import psycopg2
import simplejson as json
from decimal import Decimal
from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('time')
parser.add_argument('temp')


class HelloDBWorld(Resource):
    def get(self):
        conn = psycopg2.connect("dbname=sensordb user=mialatal")
        cur = conn.cursor()
        cur.execute("SELECT * FROM temperatures;")
        temps = cur.fetchall()
        cur.close()
        conn.close()
        print(temps)
        return json.dumps(temps)

    def put(self):
        args = parser.parse_args()
        try:
            time = str(args['time'])
            print('timedone')
            temp = str(args['temp'])
            conn = psycopg2.connect("dbname=sensordb user=mialatal")
            cur = conn.cursor()
            print(cur.mogrify("INSERT INTO temperatures(time, temp) \
                        VALUES(%s,%s);", (time, temp)))
            # cur.execute("INSERT INTO temperatures(time, temp) \
            #            VALUES(%s,%s);", (time, temp))
            cur.close()
            conn.close()
        except Exception as e:
            return e, 418
        return "success", 200


api.add_resource(HelloDBWorld, '/api/temps')


app.run(host='10.0.2.15')
