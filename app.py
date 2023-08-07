import streamlit as st
from fetch_file import fetch_github_repositories


def user_input():
    st.title('Github Automated Analysis')
    url = st.text_input("Please Enter The GitHub User's URL")
    return url

def main():
    st.title("Welcome to the GitHub Repository Analyzer")   
    st.write("""This Python-based tool is designed to help you find the most technically complex and challenging repository from a given GitHub user's profile. Just enter the GitHub user's URL in the input box below and click the "Enter" to get started.""")

    st.write("""Once you enter the URL, our tool tool uses GPT and LangChain to assess each repository individually and find the most challenging one.""")
             
    st.write("""After analyzing all the repositories, the tool will determine and display the most technically challenging repository, allowing you to gain insights into the user's most sophisticated work.""")
             
    st.write("""We hope this tool helps you discover exceptional repositories and connect with top-notch developers in the GitHub community.""")

    st.write("Get started now. Happy exploring!")


    github_url = user_input()

    if github_url:
        most_complex_repository_name, most_complex_repository_link = fetch_github_repositories(github_url)

        if most_complex_repository_name and most_complex_repository_link:
            st.write(f"The most technically complex repository from user '{github_url}' is '{most_complex_repository_name}'.\n")
            st.write(f"Here is the direct link to the repository: [{most_complex_repository_name}]({most_complex_repository_link})")
        else:
            st.write("Oops!!! Some Error Occurred")

if __name__ == "__main__":
    main()