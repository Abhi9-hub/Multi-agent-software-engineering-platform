from pathlib import Path

class FileManager:
    def save(self, filename: str, content: str):
        output_dir = Path("workspace")
        output_dir.mkdir(exist_ok=True)

        file_path = output_dir / filename

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        
        print(f"[FileManger] Saved -> {file_path}")
        return file_path
