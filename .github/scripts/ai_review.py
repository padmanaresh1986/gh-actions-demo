import os
import openai
import requests

GITHUB_API = "https://api.github.com"
REPO = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("PR_NUMBER")

def get_diff():
    url = f"{GITHUB_API}/repos/{REPO}/pulls/{PR_NUMBER}/files"
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    response = requests.get(url, headers=headers)
    files = response.json()
    diff = ""
    for file in files:
        diff += f"\nFile: {file['filename']}\n{file.get('patch', '')}\n"
    return diff

def get_review_comments(diff):
    prompt = f"""
    You are a senior software engineer reviewing a pull request. 
    Please analyze the following code diff and provide feedback on:
    - Code quality
    - Potential bugs
    - Naming conventions
    - Security risks
    - Suggestions for improvement

    Code Diff:
    {diff}
    """
    ait_api_key = os.getenv("AIT_API_KEY")

    # Initialize the client at the top of your file (after imports)
    client = OpenAI(
        api_key=ait_api_key,
        base_url="https://api.together.xyz/v1"
    )

    # Then modify your API call to:
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def post_comment(body):
    url = f"{GITHUB_API}/repos/{REPO}/issues/{PR_NUMBER}/comments"
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    data = {"body": body}
    requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    diff = get_diff()
    feedback = get_review_comments(diff)
    post_comment(feedback)
