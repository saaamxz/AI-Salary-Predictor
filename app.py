from flask import Flask, render_template, request

app = Flask(__name__)

# مسار عرض الصفحة أول مرة (GET) أو حساب النتيجة عند الضغط على الزر (POST)
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    exp_value = ""
    rating_value = ""
    
    if request.method == 'POST':
        try:
            # سحب البيانات المدخلة
            exp = float(request.form['experience'])
            rating = float(request.form['rating'])
            
            # حفظ القيم المدخلة عشان ما تلمسحش بعد الـ Submit
            exp_value = request.form['experience']
            rating_value = request.form['rating']
            
            # حساب الحسبة الافتراضية للموديل
            predicted_salary = 2000 + (exp * 500) + (rating * 300)
            prediction = "{:,.0f}".format(predicted_salary)
        except Exception as e:
            print("Error:", e)
            
    # إرسال كل البيانات للواجهة في نفس الصفحة بدون الانتقال لمسار خارجي
    return render_template('model_form.html', prediction=prediction, exp_value=exp_value, rating_value=rating_value)

if __name__ == '__main__':
    app.run(debug=True, port=5000)