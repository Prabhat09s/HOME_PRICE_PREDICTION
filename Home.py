import streamlit as st
import os
from PIL import Image

import sklearn
print(sklearn.__version__)


st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)


#st.write("# Welcome to Streamlit! 👋")

# image_folder = "images"
# image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# image_files.sort()
#
# # Add a slider
# index = st.slider("Slide through images", 0, len(image_files) - 1, 0)
#
# # Display current image
# st.image(Image.open(image_files[index]), use_container_width=True)

# st.image("images/img1.jpg", caption="Sunrise by the mountains")


# app.py

# import base64
# import pathlib
# import mimetypes
# import streamlit.components.v1 as components
#
# st.set_page_config(page_title="Image Carousel", layout="centered")
#
# IMAGE_FOLDER = "images"  # relative to where you run `streamlit run app.py`
#
# # Collect image files
# p = pathlib.Path(IMAGE_FOLDER)
# image_files = [str(x) for x in sorted(p.iterdir()) if x.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".webp")]
#
# if not image_files:
#     st.error(f"No images found in folder '{IMAGE_FOLDER}'. Put your images there and re-run.")
#     st.stop()
#
# # Convert images to base64 data URIs
# data_uris = []
# for fp in image_files:
#     mime_type, _ = mimetypes.guess_type(fp)
#     if not mime_type:
#         mime_type = "image/jpeg"
#     with open(fp, "rb") as f:
#         b64 = base64.b64encode(f.read()).decode()
#         data_uris.append(f"data:{mime_type};base64,{b64}")
#
# # Build HTML + CSS + JS (dots + prev/next + autoplay)
# carousel_images_html = "\n".join(
#     f'<div class="mySlides fade"><img src="{uri}" style="width:100%; height:100%; object-fit:contain; border-radius:12px;"></div>'
#     for uri in data_uris
# )
#
# dots_html = "".join([f'<span class="dot" onclick="currentSlide({i+1})"></span>' for i in range(len(data_uris))])
#
# html = f"""
# <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8">
# <style>
# * {{box-sizing:border-box}}
# .mySlides {{display:none; height:100%;}}
# .slideshow-container {{
#   max-width: 900px;
#   height: 520px;
#   position: relative;
#   margin: auto;
#   background: #111;
#   padding: 12px;
#   border-radius: 14px;
# }}
# .prev, .next {{
#   cursor: pointer;
#   position: absolute;
#   top: 50%;
#   width: auto;
#   padding: 12px;
#   margin-top: -24px;
#   color: white;
#   font-weight: bold;
#   font-size: 20px;
#   transition: 0.3s;
#   user-select: none;
#   background-color: rgba(0,0,0,0.35);
#   border-radius: 6px;
# }}
# .next {{ right: 10px; }}
# .prev {{ left: 10px; }}
# .prev:hover, .next:hover {{ background-color: rgba(0,0,0,0.6); }}
# .dot {{ cursor:pointer; height:12px; width:12px; margin:0 4px; background:#bbb; border-radius:50%; display:inline-block; transition: background 0.3s; }}
# .active, .dot:hover {{ background:#717171; }}
# .fade {{ animation-name: fade; animation-duration: 0.8s; }}
# @keyframes fade {{ from {{opacity:.4}} to {{opacity:1}} }}
# </style>
# </head>
# <body>
# <div class="slideshow-container">
# {carousel_images_html}
#
# <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
# <a class="next" onclick="plusSlides(1)">&#10095;</a>
# </div>
# <br />
# <div style="text-align:center">{dots_html}</div>
#
# <script>
# let slideIndex = 1;
# let slideTimer = null;
# showSlides(slideIndex);
#
# function plusSlides(n) {{
#   showSlides(slideIndex += n);
#   resetTimer();
# }}
#
# function currentSlide(n) {{
#   showSlides(slideIndex = n);
#   resetTimer();
# }}
#
# function showSlides(n) {{
#   const slides = document.getElementsByClassName("mySlides");
#   const dots = document.getElementsByClassName("dot");
#   if (!slides.length) return;
#   if (n > slides.length) slideIndex = 1;
#   if (n < 1) slideIndex = slides.length;
#   for (let i = 0; i < slides.length; i++) slides[i].style.display = "none";
#   for (let i = 0; i < dots.length; i++) dots[i].className = dots[i].className.replace(" active", "");
#   slides[slideIndex-1].style.display = "block";
#   if (dots[slideIndex-1]) dots[slideIndex-1].className += " active";
# }}
#
# function autoSlide() {{
#   plusSlides(1);
# }}
#
# function resetTimer() {{
#   if (slideTimer) clearInterval(slideTimer);
#   slideTimer = setInterval(autoSlide, 3000);
# }}
#
# // start autoplay
# resetTimer();
# </script>
# </body>
# </html>
# """
#
# # Render safe HTML with JS via components
# components.html(html, height=600, scrolling=


import base64
import mimetypes
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="SmartHome Price Predictor", layout="wide")

# Title
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        color: #2E8B57;
        margin-top: 20px;
        text-shadow: 1px 1px 2px #aaa;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    <div class="title">🏡 SmartHome Price Predictor</div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Image folder and quote setup
IMAGE_FOLDER = "images"
QUOTES = [
    "Turning data into decisions — predict your dream home's worth!",
    "Smart pricing for smarter living.",
    "Your next home, powered by Machine Learning.",
    "From features to future — know the price before you buy!",
    "AI knows the value. You make the move."
]

image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
image_files.sort()

if not image_files:
    st.error("No images found in the 'images' folder.")
else:
    # Encode images to base64
    data_uris = []
    for img in image_files:
        path = os.path.join(IMAGE_FOLDER, img)
        mime_type, _ = mimetypes.guess_type(path)
        if not mime_type:
            mime_type = "image/jpeg"
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        data_uris.append(f"data:{mime_type};base64,{b64}")

    # Create carousel with text
    carousel_html = ""
    for i, img_uri in enumerate(data_uris):
        quote = QUOTES[i % len(QUOTES)]
        carousel_html += f"""
        <div class="mySlides fade">
            <img src="{img_uri}" style="width:100%; border-radius:12px; object-fit:cover; height:450px;">
            <div class="quote">{quote}</div>
        </div>
        """

    html_code = f"""
    <style>
    * {{box-sizing: border-box;}}
    .slideshow-container {{
        position: relative;
        max-width: 900px;
        margin: auto;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }}
    .mySlides {{display:none;}}
    .fade {{
        animation-name: fade;
        animation-duration: 2.5s;
    }}
    @keyframes fade {{
        from {{opacity: .4}} 
        to {{opacity: 1}}
    }}
    .quote {{
        position: absolute;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0,0,0,0.4);
        color: #fff;
        font-size: 20px;
        padding: 10px 25px;
        border-radius: 20px;
        font-weight: 500;
        text-align: center;
        width: 80%;
        animation: slideUp 2s ease-in-out;
    }}
    @keyframes slideUp {{
        from {{transform: translate(-50%, 30px); opacity: 0;}}
        to {{transform: translate(-50%, 0); opacity: 1;}}
    }}
    </style>

    <div class="slideshow-container">
        {carousel_html}
    </div>

    <script>
    let slideIndex = 0;
    showSlides();
    function showSlides() {{
        let slides = document.getElementsByClassName("mySlides");
        for (let i = 0; i < slides.length; i++) {{
            slides[i].style.display = "none";
        }}
        slideIndex++;
        if (slideIndex > slides.length) {{slideIndex = 1}}
        slides[slideIndex-1].style.display = "block";
        setTimeout(showSlides, 4000); // Change image every 4 seconds
    }}
    </script>
    """

    components.html(html_code, height=500, scrolling=False)

# Add a call-to-action section
st.markdown(
    """
    <div style='text-align:center; margin-top:40px;'>
        <h2 style='color:#006400;'>🔍 Explore, Predict, and Discover</h2>
        <p style='font-size:18px; color:#444;'>
            Upload your property details or choose parameters to find out your house or apartment’s predicted market value — 
            powered by the magic of Machine Learning.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)



st.sidebar.success("Select a demo above.")