import wikipedia


def search_wikipedia():
    while True:
        # Prompt the user for a page title or search phrase
        search_query = input("Enter page title: ")

        if search_query == "":
            # Exit the loop if the user enters a blank input
            print("Thank you.")
            break

        try:
            # Search for the page with autosuggest turned off
            page = wikipedia.page(search_query, auto_suggest=False)
            print(f"\n{page.title}\n")
            print(f"{wikipedia.summary(search_query, sentences=3, auto_suggest=False)}\n")
            print(f"{page.url}\n")
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation errors (multiple results for a search query)
            print(f"We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:7])  # Show first 7 options
        except wikipedia.exceptions.PageError:
            # Handle cases where no page matches the search query
            print(f"Page id \"{search_query}\" does not match any pages. Try another id!")
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    search_wikipedia()
