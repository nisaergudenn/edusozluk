from flask import Flask, render_template

app = Flask('app')

basliklar = [
    {
        "id": 1,
        "baslik": "python eğitimi",
        "yazilar": ["yazi1", "yazi2", "yazi3"]
    },
    {
        "id": 2,
        "baslik": "resmi bayramlar",
        "yazilar": ["yazi11", "yazi22", "yazi3"]
    },
    {
        "id": 3,
        "baslik": "zamlar",
        "yazilar": ["yazi111", "yazi222", "yazi333"]
    },
    {
        "id": 4,
        "baslik": "2024 trendler",
        "yazilar": ["yazi1111", "yazi2222", "yazi3333"]
    }
]

@app.route('/')
def home_page():
    return render_template("ana_sayfa.html", basliklar=basliklar)

@app.route('/baslik/<int:baslik_id>')
def baslik_goster(baslik_id):
    baslik = ""
    yazilar = []

    for b in basliklar:
        if b["id"] == int(baslik_id):
            baslik = b["baslik"]
            yazilar = b["yazilar"]

    return render_template("baslik_icerik.html", baslik=baslik, yazilar=yazilar)

app.run(debug=True, host='0.0.0.0', port=8080)
