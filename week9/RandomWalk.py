import numpy as np
import matplotlib.pyplot as plt

class RandomWalk:
    def __init__(self, m_trajectories=200, t_length=100):
        self.M = m_trajectories
        self.T = t_length
        self.steps = None
        self.positions = None

    def generate(self):
        self.steps = np.random.choice([-1, 1], size=(self.M, self.T))
        initial_pos = np.zeros((self.M, 1))
        cumulative_sum = np.cumsum(self.steps, axis=1)
        self.positions = np.hstack([initial_pos, cumulative_sum])
        return self.positions

    def plot_trajectories(self, num_to_plot=5):
        if self.positions is None:
            print("Сначала сгенерируйте данные методом .generate()")
            return
        plt.figure(figsize=(10, 6))
        for i in range(min(num_to_plot, self.M)):
            plt.plot(self.positions[i], alpha=0.8, label=f"Траектория {i + 1}")
        plt.title(f"Случайное блуждание: {num_to_plot} из {self.M} траекторий")
        plt.xlabel("Шаги (T)")
        plt.ylabel("Позиция")
        plt.axhline(0, color='black', linewidth=1, linestyle='--')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.show()