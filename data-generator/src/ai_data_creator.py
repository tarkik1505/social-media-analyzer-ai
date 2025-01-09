import json
import random
import datetime
from random import randint
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the pre-trained language model (e.g., GPT-2)
model_name = "gpt2"  # You can choose other models like "distilgpt2", "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_random_date(start_date, end_date):
  """Generates a random date between the specified start and end dates."""
  time_between_dates = end_date - start_date
  days_between_dates = time_between_dates.days
  random_number_of_days = random.randrange(days_between_dates)
  random_date = start_date + datetime.timedelta(days=random_number_of_days)
  return random_date

def generate_random_time():
  """Generates a random time in the format HH:MM:SS."""
  return f"{randint(0, 23):02d}:{randint(0, 59):02d}:{randint(0, 59):02d}"

def generate_random_shortcode():
  """Generates a random shortcode for Instagram."""
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
  return "".join(random.choice(chars) for _ in range(11))

def generate_random_mediaid():
  """Generates a random media ID."""
  return random.randint(1000000000000000000, 9999999999999999999)

def generate_random_location():
  """Generates a random location (placeholder)."""
  locations = ["Home", "Office", "Gym", "Cafe", "Beach", "Park", "Travel", "Restaurant", "City", "Nature"]
  return random.choice(locations)

def generate_random_hashtags(category):
  """Generates relevant hashtags based on the category."""
  hashtags = {
      "Fitness": ["#Fitness", "#GymLife", "#Workout", "#Health", "Exercise", "FitFam", "StrongNotSkinny"],
      "Food": ["#Food", "#Foodie", "#FoodPorn", "Cooking", "Recipe", "Tasty", "YUM"],
      "Travel": ["#Travel", "Wanderlust", "Travelgram", "Instatravel", "Explore", "Vacation", "Adventure"],
      "Meditation": ["#Meditation", "Mindfulness", "Yoga", "Zen", "Spiritual", "Peace", "InnerPeace"],
      "Finance": ["#Finance", "#Investing", "Money", "Business", "Startup", "FinancialFreedom", "Wealth"],
      "Politics": ["#Politics", "SocialJustice", "HumanRights", "Equality", "Change", "Activism", "Vote"],
      "Family": ["#Family", "Love", "FamilyTime", "Blessed", "Together", "Memories", "Happiness"]
  }
  return random.sample(hashtags[category], random.randint(2, 5))

def generate_ai_caption(category):
  """Generates a caption using the language model."""
  prompts = [
      f"Write a short, engaging Instagram caption about {category}.",
      f"Give me a creative caption for a {category} post.",
      f"Come up with a catchy caption for an Instagram photo related to {category}."
  ]
  prompt = random.choice(prompts)

  input_ids = tokenizer.encode(prompt, return_tensors="pt")
  output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2)
  caption = tokenizer.decode(output[0], skip_special_tokens=True)
  return caption

def generate_instagram_post(category):
  """Generates a single Instagram post dictionary."""
  start_date = datetime.datetime(2023, 1, 1)
  end_date = datetime.datetime(2024, 1, 31)
  date_utc = generate_random_date(start_date, end_date)
  date_local = date_utc + datetime.timedelta(hours=5, minutes=30)
  current_type = random.choice(["Static Image", "Reel", "Carousel"])

  post = {
      "date_utc": date_utc.strftime("%Y-%m-%d %H:%M:%S"),
      "shortcode": generate_random_shortcode(),
      "caption": generate_ai_caption(category),
      "comments": randint(100, 5000),
      "sponsor_users": [],
      "date": date_utc.strftime("%Y-%m-%d %H:%M:%S"),
      "caption_hashtags": [f"#{tag}" for tag in generate_random_hashtags(category)],
      "title": "",
      "tagged_users": [],
      "typename": current_type,
      "video_view_count": randint(0, 1000000) if "Reel" in current_type else "",
      "likes": randint(100, 100000),
      "owner_username": "indian_best_podcaster",
      "is_pinned": random.choice([True, False]),
      "mediaid": generate_random_mediaid(),
      "date_local": date_local.strftime("%Y-%m-%d %H:%M:%S+%z"),
      "profile": "indian_best_podcaster",
      "caption_mentions": [],
      "video_duration": randint(0, 60) if "Reel" in current_type else "",
      "is_video": True if "GraphVideo" in current_type else False,
      "mediacount": randint(1, 10) if "Carousel" in current_type else 1,
      "is_sponsored": False,
      "location": generate_random_location()
  }
  return post

if __name__ == "__main__":
  categories = ["Fitness", "Food", "Travel", "Meditation", "Finance", "Politics", "Family"]
  data = []

  for _ in range(5000):
      category = random.choice(categories)
      data.append(generate_instagram_post(category))

  with open("instagram_posts_with_ai_captions_2.json", "w") as outfile:
      json.dump(data, outfile, indent=4)

  print("1000 Instagram posts with AI-generated captions saved to instagram_posts_with_ai_captions.json")