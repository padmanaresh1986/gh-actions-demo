### **Workshop Script**

#### **1. Introduction (5 minutes)**
- **Welcome Participants:**
  - "Good [morning/afternoon], everyone! Welcome to this workshop on **GitHub Actions**. My name is [Your Name], and I’m excited to guide you through the world of automation with GitHub Actions."
  - "Whether you’re a developer, DevOps engineer, or just someone curious about CI/CD, this workshop will help you understand how GitHub Actions can streamline your workflows."

- **Agenda Overview:**
  - "Here’s what we’ll cover today:
    1. What is GitHub Actions?
    2. Setting up workflows.
    3. Understanding triggers and events.
    4. Using actions from the Marketplace.
    5. Advanced topics like matrix builds and secrets management.
    6. A live Q&A session at the end."

- **Prerequisites:**
  - "Before we dive in, make sure you have:
    - A GitHub account.
    - Basic knowledge of Git and YAML syntax.
    - Your laptop ready to follow along with examples."

---

#### **2. What is GitHub Actions? (10 minutes)**
- **Explain GitHub Actions:**
  - "GitHub Actions is a powerful CI/CD tool integrated into GitHub. It allows you to automate tasks like testing, building, and deploying code directly from your repository."
  - "It’s like having a personal assistant that runs workflows whenever specific events happen, such as pushing code or opening pull requests."

- **Why Use GitHub Actions?**
  - "GitHub Actions is seamless, free for public repositories, and has a rich ecosystem of pre-built actions. Plus, it eliminates the need to manage external CI/CD tools."

- **Key Concepts:**
  - "Let’s define some key terms:
    - **Workflow:** An automated process defined in a YAML file.
    - **Jobs:** A set of steps that run in a specific environment.
    - **Steps:** Individual commands or tasks within a job.
    - **Actions:** Reusable components for common tasks.
    - **Runners:** Machines that execute workflows."

---

#### **3. Setting Up GitHub Actions (20 minutes)**
- **Creating a Workflow File:**
  - "Workflows are stored in `.github/workflows/` and written in YAML format. Let’s create a simple workflow together."
  - "This workflow will print 'Hello, World!' every time you push code to the main branch."

- **Live Demo:**
  - Walk participants through creating a `hello-world.yml` file:
    ```yaml
    name: Hello World Workflow

    on:
      push:
        branches:
          - main

    jobs:
      hello-world:
        runs-on: ubuntu-latest
        steps:
          - name: Print Hello World
            run: echo "Hello, World!"
    ```
  - "Commit this file to your repository and watch the workflow run automatically!"

- **Hands-On Activity:**
  - "Now it’s your turn! Create a similar workflow in your own repository and test it out."

---

#### **4. Understanding Triggers and Events (20 minutes)**
- **Common Triggers:**
  - "GitHub Actions supports various triggers, such as:
    - `push`: Runs when code is pushed.
    - `pull_request`: Runs when a pull request is opened.
    - `schedule`: Runs at specific times using cron syntax."

- **Demo: Trigger on Pull Requests:**
  - "Let’s create a workflow that runs tests whenever a pull request is opened."
  - Show this example:
    ```yaml
    name: Pull Request Tests

    on:
      pull_request:
        branches:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout Code
            uses: actions/checkout@v3
          - name: Run Tests
            run: echo "Running tests..."
    ```

- **Hands-On Activity:**
  - "Try creating this workflow in your repository and open a pull request to see it in action."

---

#### **5. Using Actions from the Marketplace (20 minutes)**
- **What are Actions?**
  - "Actions are reusable units of code that simplify complex tasks. You can find them in the GitHub Actions Marketplace."

- **Popular Actions:**
  - Highlight actions like:
    - `actions/checkout`: Check out repository code.
    - `actions/setup-node`: Set up Node.js environments.
    - `peaceiris/actions-gh-pages`: Deploy to GitHub Pages.

- **Demo: Automate Node.js Deployment:**
  - "Let’s deploy a Node.js app to GitHub Pages using pre-built actions."
  - Show this example:
    ```yaml
    name: Deploy Node.js App

    on:
      push:
        branches:
          - main

    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout Code
            uses: actions/checkout@v3
          - name: Setup Node.js
            uses: actions/setup-node@v3
            with:
              node-version: '16'
          - name: Install Dependencies
            run: npm install
          - name: Build Project
            run: npm run build
          - name: Deploy to GitHub Pages
            uses: peaceiris/actions-gh-pages@v3
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              publish_dir: ./build
    ```

- **Hands-On Activity:**
  - "Follow along and deploy your own Node.js app!"

---

#### **6. Advanced Topics (30 minutes)**
- **Matrix Builds:**
  - "Matrix builds allow you to run jobs across multiple configurations, such as different operating systems or Node.js versions."
  - Show an example:
    ```yaml
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        node-version: [14, 16]
    ```

- **Secrets Management:**
  - "Use GitHub Secrets to store sensitive data like API keys securely."
  - Access secrets in workflows using `${{ secrets.SECRET_NAME }}`.

- **Self-Hosted Runners:**
  - "For private environments, you can use self-hosted runners instead of GitHub-hosted ones."

- **Reusing Workflows:**
  - "You can call one workflow from another to avoid duplication."

---

#### **7. Q&A and Wrap-Up (15 minutes)**
- **Recap:**
  - "Today, we covered:
    - What GitHub Actions is and why it’s useful.
    - How to create workflows and use triggers.
    - Leveraging actions from the Marketplace.
    - Advanced features like matrix builds and secrets management."

- **Q&A Session:**
  - "Do you have any questions? Feel free to ask now or reach out later."

- **Additional Resources:**
  - Share links to documentation, tutorials, and forums:
    - GitHub Docs: [https://docs.github.com/actions](https://docs.github.com/actions)
    - GitHub Marketplace: [https://github.com/marketplace?type=actions](https://github.com/marketplace?type=actions)
    - Stack Overflow: [https://stackoverflow.com/questions/tagged/github-actions](https://stackoverflow.com/questions/tagged/github-actions)

- **Thank You:**
  - "Thank you for participating in this workshop! I hope you found it helpful. If you’d like to connect, here’s my email/[LinkedIn/GitHub]. Have fun automating with GitHub Actions!"

---

### **Tips for Delivery**
1. **Engage Participants:**
   - Ask questions and encourage participants to share their thoughts.
   - Use polls or quizzes if possible.

2. **Time Management:**
   - Stick to the allocated time for each section to ensure you cover everything.

3. **Be Prepared for Questions:**
   - Anticipate common questions and prepare answers in advance.

4. **Encourage Hands-On Learning:**
   - Provide clear instructions for hands-on activities and assist participants as needed.

---

This script ensures a structured and engaging workshop experience. Let me know if you’d like further refinements!