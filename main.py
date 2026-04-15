from week9.RandomWalk import RandomWalk
sim = RandomWalk(m_trajectories=200, t_length=100)
trajectories = sim.generate()

print(f"Матрица позиций готова. Размер: {trajectories.shape}")
print(f"Финальные позиции первых 5 траекторий: {trajectories[:5, -1]}")

# Визуализация
sim.plot_trajectories(num_to_plot=10)
