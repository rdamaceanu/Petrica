# app.py
from flask import Flask, render_template, request, jsonify
from database.daypart_crud import get_day_parts_in_day
from database.journal_crud import save_journal_entry, get_journal_entry

app = Flask(__name__)

@app.route('/day')
def day_view():
    return render_template('day_view.html')

@app.route('/api/dayparts')
def api_dayparts():
    day_id = request.args.get('day_id', default=1, type=int)
    day_parts = get_day_parts_in_day(day_id)

    # Fetch minitasks for each day part
    for day_part in day_parts:
        day_part_id = day_part['day_part_id']
        minitasks = get_minitasks_in_day_part(day_part_id)
        day_part['minitasks'] = minitasks

    return jsonify(day_parts)

@app.route('/api/journal', methods=['GET', 'POST'])
def api_journal():
    if request.method == 'POST':
        data = request.get_json()
        content = data.get('content', '')
        day_id = request.args.get('day_id', default=1, type=int)
        save_journal_entry(day_id, content)
        return jsonify({'status': 'success'})
    else:
        day_id = request.args.get('day_id', default=1, type=int)
        entry = get_journal_entry(day_id)
        return jsonify(entry)

if __name__ == '__main__':
    app.run(debug=True)
