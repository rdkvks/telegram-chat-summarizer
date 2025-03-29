def test_summarizer():
    from src.summarizer import Summarizer

    # Create an instance of the Summarizer
    summarizer = Summarizer()

    # Sample chat messages for testing
    chat_messages = [
        "Hello, how are you?",
        "I'm doing well, thank you!",
        "What are your plans for today?",
        "I plan to work on the Telegram bot project."
    ]

    # Expected summary output
    expected_summary = "The conversation is about well-being and project plans."

    # Generate the summary
    generated_summary = summarizer.generate_summary(chat_messages)

    # Assert that the generated summary matches the expected summary
    assert generated_summary == expected_summary, f"Expected: {expected_summary}, but got: {generated_summary}"