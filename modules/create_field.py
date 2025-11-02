# створення поля

def create_field(width=10, height=10):
    """Створює двовимірне поле як список рядків"""
    field = []
    for y in range(height):
        row = ""
        for x in range(width):
            if y == 0 or y == height - 1 or x == 0 or x == width - 1:
                row += "█"  # стіни
            else:
                row += " "  # порожнеча        
        field.append(row)
    return field