def generate_transcript():
    # List of (speaker, utterance) tuples
    lines = [
        ("Speaker A", "Hey, um, have you seen the forecast for this weekend?"),
        ("Speaker B", "No, I haven't, like, is it going to rain?"),
        ("Speaker A", "It's supposed to be sunny, you know, perfect picnic weather."),
        ("Speaker B", "Sounds great, um, where should we go?"),
        ("Speaker A", "I was thinking the lakeside park near downtown."),
        ("Speaker B", "That's a good idea. Should we invite Sarah and Mike?"),
        ("Speaker A", "Yeah, like, they love outdoor stuff."),
        ("Speaker B", "Okay, I'll text them tonight."),
        ("Speaker A", "Also, we need to bring snacks. I can bake cookies."),
        ("Speaker B", "Yum, cookies! I'll bring some lemonade."),
        ("Speaker A", "Do we need blankets or chairs?"),
        ("Speaker B", "Let's bring both, you know, just in case."),
        ("Speaker A", "Great. I'll also pack some frisbees."),
        ("Speaker B", "Perfect, uh, looking forward to it!")
    ]
    return lines

def save_transcript(lines, path="transcript.txt"):
    """
    Write the tuple list to a transcript.txt file in the required format.
    """
    with open(path, "w", encoding="utf-8") as f:
        for speaker, text in lines:
            f.write(f"{speaker}: {text}\n")

if _name_ == "_main_":
    transcript = generate_transcript()
    save_transcript(transcript)
    print(f"Wrote {len(transcript)} lines to transcript.txt")
