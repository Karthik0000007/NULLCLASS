from flask import Flask, render_template
from analytics_utils import load_data, total_queries, most_common_topics, average_satisfaction

app = Flask(__name__)

@app.route("/")
def dashboard():
    df = load_data("customer_service_interactions.csv")
    print("Columns in DataFrame:", df.columns.tolist())
    print("First 3 rows:\n", df.head(3))
    
    total = total_queries(df)
    topics = most_common_topics(df)
    avg_rating = average_satisfaction(df)
    
    return render_template("dashboard.html", total=total, topics=topics, avg_rating=avg_rating)

if __name__ == "__main__":
    app.run(debug=True)
