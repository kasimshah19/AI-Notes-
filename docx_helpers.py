import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Color Palette
NAVY = "0A2540"         # Deep Navy for primary titles & table headers
SLATE_BLUE = "1E3A8A"   # Slate Blue for section subheadings
ACCENT_RED = "991B1B"   # Deep Red for critical warnings/cutoffs
ACCENT_GREEN = "166534" # Deep Green for optimal/admissible highlights
BG_LIGHT = "F1F5F9"     # Light Slate gray background for callout boxes
BG_ZEBRA = "F8FAFC"     # Very light background for alternating table rows
BORDER_GRAY = "CBD5E1"  # Crisp subtle border

def setup_document():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.35)
        s.bottom_margin = Inches(0.35)
        s.left_margin = Inches(0.40)
        s.right_margin = Inches(0.40)
        s.page_width = Inches(8.27)   # A4 Width
        s.page_height = Inches(11.69) # A4 Height
        
        # Configure Header & Footer
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("DBATU B.TECH CSE (SEM-7) | BTCOC701: ARTIFICIAL INTELLIGENCE | MASTER OPEN-BOOK TEST AID")
        hrun.font.name = "Arial"
        hrun.font.size = Pt(6.5)
        hrun.font.color.rgb = RGBColor(100, 116, 139)
        
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun = fp.add_run("Micro-Print Ready Comprehensive Answer Sheet | Strictly 1 Page per Topic | Page ")
        frun.font.name = "Arial"
        frun.font.size = Pt(6.5)
        frun.font.color.rgb = RGBColor(100, 116, 139)
        
    return doc

def set_cell_background(cell, hex_color):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=20, bottom=20, left=40, right=40):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_page_header_banner(doc, page_num, unit_label, topic_title):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_cell_background(tbl.cell(0, 0), NAVY)
    set_cell_background(tbl.cell(0, 1), NAVY)
    set_cell_margins(tbl.cell(0, 0), top=25, bottom=25, left=60, right=60)
    set_cell_margins(tbl.cell(0, 1), top=25, bottom=25, left=60, right=60)
    
    # Left: Page Number & Title
    p0 = tbl.cell(0, 0).paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(0)
    run_p = p0.add_run(f"PAGE {page_num}: {topic_title.upper()}\n")
    run_p.font.name = "Arial"
    run_p.font.size = Pt(9.5)
    run_p.font.bold = True
    run_p.font.color.rgb = RGBColor(255, 255, 255)
    
    run_sub = p0.add_run(f"Comprehensive Model Answer & Exam Solution Bank | High-Yield Reference")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(6.5)
    run_sub.font.color.rgb = RGBColor(203, 213, 225)
    
    # Right: Unit & Page Badge
    p1 = tbl.cell(0, 1).paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(0)
    run_u = p1.add_run(f"{unit_label.upper()}\n")
    run_u.font.name = "Arial"
    run_u.font.size = Pt(8.5)
    run_u.font.bold = True
    run_u.font.color.rgb = RGBColor(253, 224, 71) # Light yellow accent
    
    run_b = p1.add_run(f"Target: Under 1 A4 Page | Micro-Print Optimized")
    run_b.font.name = "Arial"
    run_b.font.size = Pt(6.5)
    run_b.font.color.rgb = RGBColor(226, 232, 240)
    
    tbl.columns[0].width = Inches(5.8)
    tbl.columns[1].width = Inches(1.67)

def add_section_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2.5)
    p.paragraph_format.space_after = Pt(0.5)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(8.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 58, 138) # Slate Blue
    return p

def add_subheading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1.5)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(7.8)
    run.font.bold = True
    run.font.color.rgb = RGBColor(15, 23, 42)
    return p

def add_body_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1.0)
    p.paragraph_format.line_spacing = 1.05
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.font.name = "Arial"
        r_b.font.size = Pt(7.5)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(7.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_bullet_point(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0.8)
    p.paragraph_format.line_spacing = 1.04
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.font.name = "Arial"
        r_b.font.size = Pt(7.3)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(7.3)
    run.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_callout_box(doc, text, title="EXAM TIP / KEY TAKEAWAY"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(7.47)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, BG_LIGHT)
    set_cell_margins(cell, top=20, bottom=20, left=40, right=40)
    
    # Left border only (3pt)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="18" w:space="0" w:color="{SLATE_BLUE}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    r_t = p.add_run(f"[{title.upper()}] ")
    r_t.font.name = "Arial"
    r_t.font.size = Pt(7.2)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(30, 58, 138)
    
    r_txt = p.add_run(text)
    r_txt.font.name = "Arial"
    r_txt.font.size = Pt(7.2)
    r_txt.font.color.rgb = RGBColor(30, 41, 59)

def create_table_grid(doc, headers, rows, col_widths=None):
    tbl = doc.add_table(rows=len(rows)+1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders(tbl, color="CBD5E1", sz="4", val="single")
    
    # Header Row
    for j, h in enumerate(headers):
        cell = tbl.cell(0, j)
        set_cell_background(cell, NAVY)
        set_cell_margins(cell, top=18, bottom=18, left=35, right=35)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run(h)
        run.font.name = "Arial"
        run.font.size = Pt(7.2)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
    
    # Data Rows
    for i, row in enumerate(rows):
        bg = BG_ZEBRA if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = tbl.cell(i+1, j)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=12, bottom=12, left=30, right=30)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.02
            run = p.add_run(str(val))
            run.font.name = "Arial"
            run.font.size = Pt(7.0)
            run.font.color.rgb = RGBColor(30, 41, 59)
            if j == 0 and len(headers) > 2:
                run.font.bold = True
    
    if col_widths:
        for j, w in enumerate(col_widths):
            tbl.columns[j].width = Inches(w)
            for cell in tbl.columns[j].cells:
                cell.width = Inches(w)
                
    return tbl

def add_ascii_diagram(doc, diagram_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(7.47)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=15, bottom=15, left=30, right=30)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            <w:left w:val="single" w:sz="6" w:space="0" w:color="{SLATE_BLUE}"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(diagram_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(6.8)
    run.font.color.rgb = RGBColor(15, 23, 42)
