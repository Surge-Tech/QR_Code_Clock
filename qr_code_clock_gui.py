import qrcode
from PIL import Image, ImageTk
import tkinter as tk
import time


def generate_qr_code(data: str) -> Image.Image:
    """Generate a QR code image from the given data."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    return qr_image.convert("RGBA")


def update_qr_code(qr_label):
    """Update the QR code in the Tkinter window every second."""
    while True:
        # Get the current time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        # Generate a QR code with the current time
        qr_image = generate_qr_code(current_time)

        # Convert PIL image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(qr_image)

        # Update the image in the label
        qr_label.config(image=tk_image)
        qr_label.image = tk_image

        # Wait for 1 second before updating again
        time.sleep(1)


def main():
    """Create the GUI window and display the QR code."""
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("QR Code Clock")

    # Set the window size
    root.geometry("400x400")

    # Create a label for the QR code
    qr_label = tk.Label(root)
    qr_label.pack(expand=True)

    # Use a separate thread for updating the QR code to keep the GUI responsive
    import threading
    threading.Thread(target=update_qr_code, args=(qr_label,), daemon=True).start()

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
