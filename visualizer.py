import pandas as pd
import matplotlib.pyplot as plt

def plot_performance(file_path='students.csv'):
    # Load dataset
    df = pd.read_csv(file_path)

    # Plot bar chart for each subject
    subjects = ['Math', 'Science', 'English']
    for subject in subjects:
        plt.figure(figsize=(8,5))
        plt.bar(df['Name'], df[subject], color='skyblue')
        plt.xticks(rotation=45)
        plt.ylabel('Marks')
        plt.title(f'Student Performance in {subject}')
        plt.tight_layout()
        plt.savefig(f'{subject}_performance.png')
        plt.close()

    print("Performance charts saved as PNG files.")

if __name__ == '__main__':
    plot_performance()
