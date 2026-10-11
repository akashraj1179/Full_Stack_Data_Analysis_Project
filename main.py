from agents.data_agent import app

if __name__ == "__main__":
    result = app.invoke({"input": "Run compliance check on latest data"})
    print(result["output"])
