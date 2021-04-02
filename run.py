from generator.app import app
from generator import views


if __name__ == "__main__":
    app.run(debug=True, port=3000)
