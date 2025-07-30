import pandas as pd

# Define input and output paths
INPUT_CSV_PATH = "data/dataset.csv"
OUTPUT_CSV_PATH = "data/filtered_books.csv"

# Genres of interest 
TARGET_GENRES = {"mystery", "fiction", "science", "anime", "romance"}

def genre_matches(genre_str):
    if pd.isna(genre_str):
        return False
    genres = {g.strip().lower() for g in genre_str.split(",")}
    return bool(TARGET_GENRES & genres)

def main():
    print("🔍 Loading dataset...")
    df = pd.read_csv(INPUT_CSV_PATH)
    df["reviews"] = pd.to_numeric(df["reviews"].astype(str).str.replace(",", ""), errors="coerce")

    print("✅ Filtering by genre and rating...")
    filtered_df = df[
        df["genre"].apply(genre_matches) &
        (df["rating"] > 3.5) &
        (df["reviews"] > 100) &
        (df["totalratings"] > 500) &
        (df["pages"] > 50)

    ]

    print(f"Original entries: {len(df)}")
    print(f"Filtered entries: {len(filtered_df)}")

    print(f"Saving filtered data to: {OUTPUT_CSV_PATH}")
    filtered_df.to_csv(OUTPUT_CSV_PATH, index=False)
    print("Done!")

if __name__ == "__main__":
    main()
