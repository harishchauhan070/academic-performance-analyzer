import pandas as pd

def analyze_performance(file_path='students.csv'):
    # Load dataset
    df = pd.read_csv(file_path)

    print("===== Academic Performance Report =====")
    print(f"Total Students: {len(df)}")

    # Subject-wise averages
    print("\nSubject-wise Averages:")
    for subject in ['Math', 'Science', 'English']:
        print(f"{subject}: {df[subject].mean():.2f}")

    # Topper overall
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    topper = df.loc[df['Total'].idxmax()]
    print("\nTopper:")
    print(f"{topper['Name']} with total {topper['Total']} marks")

if __name__ == '__main__':
    analyze_performance()
