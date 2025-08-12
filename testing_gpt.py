from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text)
