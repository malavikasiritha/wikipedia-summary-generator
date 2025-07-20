import wikipedia
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import pyttsx3

def summarize_topic(topic):
    try:
        print(f"\n🔎 Fetching summary for: {topic}")
        full_text = wikipedia.page(topic).content

        parser = PlaintextParser.from_string(full_text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary_sentences = summarizer(parser.document, 5)  # get 5 key points

        final_summary = "\n".join(str(sentence) for sentence in summary_sentences)
        
        print("\n📌 Summary of", topic)
        print("="*30)
        print(final_summary)

        # Save to file
        filename = f"{topic}_summary.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"📌 Summary of {topic}\n{'='*30}\n")
            f.write(final_summary)
        print(f"\n✅ Summary saved to {filename}")

        # Voice output: speak intro + summary
        engine = pyttsx3.init()
        engine.say(f"This is the summary of {topic}")
        engine.say(final_summary)
        engine.runAndWait()

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    topic = input("🔍 Enter a topic to search on Wikipedia: ")
    summarize_topic(topic)
