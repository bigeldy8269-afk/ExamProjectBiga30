from flask import Flask, request, jsonify
import numpy as np

class RandomWalkAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/random_walk', methods=['GET'])
        def random_walk():
            M = int(request.args.get('M', 200))
            T = int(request.args.get('T', 100))

            steps = np.random.choice([-1, 1], size=(M, T))
            positions = np.cumsum(steps, axis=1)
            final_positions = positions[:, -1]

            return jsonify({
                "mean": float(np.mean(final_positions)),
                "variance": float(np.var(final_positions))
            })

    def run(self):
        self.app.run(debug=True)