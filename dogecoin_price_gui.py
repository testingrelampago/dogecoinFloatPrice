import tkinter as tk
from plyer import notification
import requests
from PIL import Image, ImageTk

class DogecoinPriceTracker(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Doge")
        self.geometry("210x80")

        # Set the window to stay on top
        self.attributes('-topmost', True)

        # Load the favicon
        favicon = Image.open("favicon.ico")
        favicon = ImageTk.PhotoImage(favicon)

        # Set the favicon
        self.iconphoto(True, favicon)

        self.label = tk.Label(self, text="Fetching ...", font=("Arial", 14))
        self.label.pack(pady=20)

        self.update_price()

    def get_dogecoin_price(self):
        # Remember you can't make to many requests in the free version of coingecko 
        api_url = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"
        response = requests.get(api_url)
        data = response.json()
        return data['dogecoin']['usd']

    def update_price(self):
        price = self.get_dogecoin_price()
        print(f'${price}')

        self.label.config(text=f'${price}')
        notification.notify(
            title='Dogecoin Price',
            message=f'${price}',
            timeout=10
        )

        self.after(20000, self.update_price)

if __name__ == "__main__":
    app = DogecoinPriceTracker()
    app.mainloop()
