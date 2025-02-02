from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data from JSON
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)
students_marks = {student["name"]: student["marks"] for student in data["students"]}

@app.get("/api")
async def get_marks(names: list[str] = Query([])):
    marks = [students_marks.get(name, 0) for name in names]
    return {"marks": marks}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
