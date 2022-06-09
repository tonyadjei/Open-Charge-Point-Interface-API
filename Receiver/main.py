import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "app.receiver:app",
        host="127.0.0.1",
        port=9000,
        reload=True
    )