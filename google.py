import os
import requests
import pandas as pd

# Data from your table
data = {
    "NamaPengisi": [
        "Eko Sulistiarno", "Joko Suprasetyo", "Suyanto",
        "Agus Adi Kuncoro", "Wisnu Abdullah", "Teguh Suprapto",
        "Mohamad Sahlan", "Mohammad Nurul Hiba", "Rus Agus Saputro",
        "Suyanto", "Imam Safii", "Mohammad Nurul Hiba", "Hantoro",
        "Muhamad Wahib", "Mohammad Nurul Hiba", "Riyantono",
        "Edi Siswanto", "Mohammad Nurul Hiba", "Tri Wahyu", "Jatmoko",
        "Mohammad Nurul Hiba", "Tri Wahyu", "Riyantono", "Mohammad Nurul Hiba",
        "Muhammad Djazuli Ristanto", "Agus Dwi Purnomo", "Ferrry Mardiyanto",
        "TEST", "Tommy Aji Prasetyo", "Muhammad Mustofa", "Puguh Danardono"
    ],
    "Link2": [
        "https://drive.google.com/uc?id=1C6L0SMfjotucToCMhUqsMO0z3hZitI4e&export=download",
"https://drive.google.com/uc?id=1oM7s10Ok7aBmUqQPI_-BVGAdQQkEEoKf&export=download",
"https://drive.google.com/uc?id=1SSYkwJvxOMiiQsei3b0qWUOiPQBrwVWa&export=download",
"https://drive.google.com/uc?id=1-pHa1eiALww8fysJf7My_I3Ob0ar5Y1D&export=download",
"https://drive.google.com/uc?id=1LOPv-zqbU9AKwhw7WImJFT5Pqahv0zu_&export=download",
"https://drive.google.com/uc?id=18EgDN30yommU9sfOrFkehjqUFUgkeFGK&export=download",
"https://drive.google.com/uc?id=1kwYm99sHADKswlr8j3mJwMwr4DrAMsft&export=download",
"https://drive.google.com/uc?id=1w9S4OxNTxHH3l5gof1hIjHNTRlviVhwU&export=download",
"https://drive.google.com/uc?id=1-qb4gdvmQYfWZZl7nLxwSSygUw9DlMA3&export=download",
"https://drive.google.com/uc?id=1XqwDsWecJn90E-xoXxXFDsfKbGVVLe6S&export=download",
"https://drive.google.com/uc?id=1daXEnJypMJNVLlCuanrygYRsgWNw-ZqD&export=download",
"https://drive.google.com/uc?id=128M4GqY0SFxxylFur4ONbvre-d2agfHs&export=download",
"https://drive.google.com/uc?id=1F_gvmrVXiu0pRpmbc6xZ-0OYqgeS_Ehg&export=download",
"https://drive.google.com/uc?id=1jY3bMb66lo8DhBNdKynS6ZAcYshLgKiW&export=download",
"https://drive.google.com/uc?id=1L5CWcbeXBfmbbZCg8amU6lusembSC1gH&export=download",
"https://drive.google.com/uc?id=1f4UO_NLDqhL4--GfXBGs6GkKQCRAmVeG&export=download",
"https://drive.google.com/uc?id=1VAy91O_Wyfv8xqxjxc-YbSP0CmmYkwx-&export=download",
"https://drive.google.com/uc?id=1ugxhS3YtBlNk_XKPfbXITFcsvh7H3r-D&export=download",
"https://drive.google.com/uc?id=1KgRjpnsduOVd8Fhrr5a-nejJcF1W59hL&export=download",
"https://drive.google.com/uc?id=1Lj7Sq_67ErEg5EHYkdByviwXD0ql1Ocj&export=download",
"https://drive.google.com/uc?id=1OyJ8vilTOd-nWp-6VqiohvM_mokwCK6Z&export=download",
"https://drive.google.com/uc?id=1qaeDV0quU4Si6nbgzp354ohPBlEABeiW&export=download",
"https://drive.google.com/uc?id=1Fib0zkcTnEaVJaagJiQRSxH5zJbRiT2Y&export=download",
"https://drive.google.com/uc?id=1155mY0v8XoVjMOSq1q3q5p_O4o3HqhBy&export=download",
"https://drive.google.com/uc?id=198KwzRZOZGMD4sadoEmo4TXeRQ0AaYZ9&export=download",
"https://drive.google.com/uc?id=1qVLoeMLZkdbVizo8PcpLr-G1UbNIeHRq&export=download",
"https://drive.google.com/uc?id=1GGhwD60qyo-9rfcJXpNHNy8KtT3GNX43&export=download",
"https://drive.google.com/uc?id=1fbhzvhjc3vWjKqosnNnx6iSKu4i8tLC2&export=download",
"https://drive.google.com/uc?id=1tmZ0rIT00neE2kZMHsXjHXbtokStmhTb&export=download",
"https://drive.google.com/uc?id=1OQ7v9WYwofirpUXPktx2oR7nUsm2iPE4&export=download",
"https://drive.google.com/uc?id=1QjxfC-2qQguoEXYCrbUysFsK4pEqyjMm&export=download"




    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Folder to save images
output_folder = "downloaded_images"
os.makedirs(output_folder, exist_ok=True)

# Download images from Link4
for index, row in df.iterrows():
    name = row['NamaPengisi'].replace(" ", "_")  # Use underscore for spaces in filenames
    link = row['Link2']
    file_path = os.path.join(output_folder, f"{name}.jpg")

    try:
        print(f"Downloading {link} as {file_path}")
        response = requests.get(link)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Save the image
        with open(file_path, "wb") as f:
            f.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {link}: {e}")