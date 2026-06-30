# from transformers import AutoTokenizer, AutoModelForCausalLM


# class StoryGenerator:
#     """
#     A class to load the GPT-2 model and generate stories.
#     """

#     def __init__(self):
#         print("Loading GPT-2 model...")

#         # Load tokenizer
#         self.tokenizer = AutoTokenizer.from_pretrained("gpt2-medium")

#         # Load model
#         self.model = AutoModelForCausalLM.from_pretrained("gpt2-medium")

#         print("GPT-2 model loaded successfully!")

#     def generate_story(
#     self,
#     prompt,
#     genre="Fantasy",
#     story_length="Medium",
#     temperature=0.8,
#     top_k=50,
#     top_p=0.95,
#     num_stories=1
# ):
#         """
#         Generate one or more stories based on the user's prompt and genre.
#         """

#         final_prompt = f"""
#         You are a creative storyteller.

#         Write an original {genre.lower()} story.

#         The story should have:
#         - Interesting characters
#         - A clear beginning
#         - An exciting middle
#         - A satisfying ending

#         Story Prompt:
#         {prompt}

#         Story:
#         """

#         # Story Length Selection
#         if story_length == "Short":
#             max_length = 100

#         elif story_length == "Medium":
#             max_length = 200

#         else:
#             max_length = 300

#         # Convert prompt into tokens
#         inputs = self.tokenizer(
#             final_prompt,
#             return_tensors="pt"
#         )

#         stories = []

#         # Generate multiple stories
#         for _ in range(num_stories):

#             output = self.model.generate(
#                 input_ids=inputs["input_ids"],
#                 attention_mask=inputs["attention_mask"],
#                 max_length=max_length,
#                 temperature=0.9,
#                 top_k=40,
#                 top_p=0.92,
#                 do_sample=True,
#                 repetition_penalty=1.3,
#                 no_repeat_ngram_size=3,
#                 eos_token_id=self.tokenizer.eos_token_id,
#                 pad_token_id=self.tokenizer.eos_token_id
#             )

#             generated_text = self.tokenizer.decode(
#                 output[0],
#                 skip_special_tokens=True
#             )

#             story = generated_text[len(final_prompt):].strip()
#             stories.append(story)

            

#         return stories


from transformers import AutoTokenizer, AutoModelForCausalLM


class StoryGenerator:
    """
    AI Dungeon Story Generator using GPT-Neo 125M
    """

    def __init__(self):
        print("Loading GPT-Neo model...")

        model_name = "EleutherAI/gpt-neo-125M"

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Load model
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        # Set pad token
        self.tokenizer.pad_token = self.tokenizer.eos_token

        print("GPT-Neo model loaded successfully!")

    def generate_story(
        self,
        prompt,
        genre="Fantasy",
        story_length="Medium",
        temperature=0.9,
        top_k=50,
        top_p=0.95,
        num_stories=1
    ):

        # -----------------------------
        # Story Length
        # -----------------------------
        if story_length == "Short":
            max_new_tokens = 100

        elif story_length == "Medium":
            max_new_tokens = 200

        else:
            max_new_tokens = 300

        # -----------------------------
        # Better Prompt
        # -----------------------------
        final_prompt = f"""
Genre: {genre}

Write an engaging {genre.lower()} story.

Story starts here:

{prompt}

Continue the story naturally with interesting characters,
dialogues, emotions, adventure and a satisfying ending.

Story:
"""

        # Tokenize input
        inputs = self.tokenizer(
            final_prompt,
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        stories = []

        for _ in range(num_stories):

            output = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
                repetition_penalty=1.2,
                no_repeat_ngram_size=3,
                eos_token_id=self.tokenizer.eos_token_id,
                pad_token_id=self.tokenizer.eos_token_id,
            )

            generated_text = self.tokenizer.decode(
                output[0],
                skip_special_tokens=True
            )

            # Remove prompt from output
            story = generated_text.replace(final_prompt, "").strip()

            stories.append(story)

        return stories