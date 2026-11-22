import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

NAVY = "0A2540"
SLATE = "1E3A8A"
CHARCOAL = "0F172A"
BODY_COLOR = "1E293B"
BG_LIGHT = "F1F5F9"

def set_cell_background(cell, hex_color):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=16, bottom=16, left=35, right=35):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
    tcPr.append(tcMar)

def create_doc():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.35)
        s.bottom_margin = Inches(0.35)
        s.left_margin = Inches(0.40)
        s.right_margin = Inches(0.40)
        s.page_width = Inches(8.27)
        s.page_height = Inches(11.69)
        
        # Header
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("DBATU B.TECH CSE (SEM-7) | BTCOC701: ARTIFICIAL INTELLIGENCE | PYQ ANSWER BANK (FONT 14)")
        hrun.font.name = "Arial"
        hrun.font.size = Pt(8)
        hrun.font.color.rgb = RGBColor(100, 116, 139)
        
        # Footer
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun = fp.add_run("1-Page-Per-Answer Architecture | High-Yield Open-Book Exam Aid | Page ")
        frun.font.name = "Arial"
        frun.font.size = Pt(8)
        frun.font.color.rgb = RGBColor(100, 116, 139)
    return doc

def add_header_badge(doc, q_num, unit_str, pyq_ref):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(5.1)
    tbl.columns[1].width = Inches(2.37)
    
    set_cell_background(tbl.cell(0, 0), NAVY)
    set_cell_background(tbl.cell(0, 1), NAVY)
    set_cell_margins(tbl.cell(0, 0), top=14, bottom=14, left=30, right=30)
    set_cell_margins(tbl.cell(0, 1), top=14, bottom=14, left=30, right=30)
    
    p0 = tbl.cell(0, 0).paragraphs[0]
    p0.paragraph_format.space_before = Pt(0)
    p0.paragraph_format.space_after = Pt(0)
    r0 = p0.add_run(f"QUESTION {q_num}: {unit_str.upper()}")
    r0.font.name = "Arial"
    r0.font.size = Pt(11)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(255, 255, 255)
    
    p1 = tbl.cell(0, 1).paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(pyq_ref)
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(253, 224, 71)

def add_question_box(doc, q_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(7.47)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, BG_LIGHT)
    set_cell_margins(cell, top=16, bottom=16, left=30, right=30)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="18" w:space="0" w:color="{SLATE}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    
    r_lbl = p.add_run("QUESTION: ")
    r_lbl.font.name = "Arial"
    r_lbl.font.size = Pt(14)
    r_lbl.font.bold = True
    r_lbl.font.color.rgb = RGBColor(10, 37, 64)
    
    r_txt = p.add_run(q_text)
    r_txt.font.name = "Arial"
    r_txt.font.size = Pt(14)
    r_txt.font.bold = True
    r_txt.font.color.rgb = RGBColor(30, 58, 138)

def add_ans_header(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2.5)
    p.paragraph_format.space_after = Pt(1.0)
    r = p.add_run("ANSWER:")
    r.font.name = "Arial"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.underline = True
    r.font.color.rgb = RGBColor(15, 23, 42)

def add_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1.8)
    p.paragraph_format.line_spacing = 1.05
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.font.name = "Arial"
        r_b.font.size = Pt(14)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1.8)
    p.paragraph_format.line_spacing = 1.05
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.font.name = "Arial"
        r_b.font.size = Pt(14)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(30, 41, 59)
    return p

# ==================== PAGE BUILDERS ====================

def page_1(doc):
    add_header_badge(doc, 1, "Unit 1: Introduction to AI", "Winter 2025 (Q2.B) / Summer 2024 (Q1.A)")
    add_question_box(doc, "What is Artificial Intelligence? Discuss its relationship with the environment (PEAS framework) and state its future scope and major applications. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Artificial Intelligence (AI) is the science of designing rational agents that perceive their environment and select actions that maximize their expected performance measure. Modern AI focuses on Acting Rationally through the mapping function f: P* -> A.", "1. Definition & Philosophy:")
    add_p(doc, "An agent interacts with its environment in a continuous loop: Sensors receive percepts, the Agent Program processes them, and Actuators execute actions affecting the environment. Rationality depends on the PEAS framework.", "2. Agent-Environment Loop:")
    add_bullet(doc, "Performance Measure (P): Safety, legal speed, passenger comfort, and fuel efficiency.", "• Automated Taxi PEAS:")
    add_bullet(doc, "Environment (E): Public roads, vehicular traffic, pedestrians, and changing weather.", "")
    add_bullet(doc, "Actuators (A): Steering wheel, throttle, brakes, turn indicators, and display.", "")
    add_bullet(doc, "Sensors (S): Video cameras, LiDAR, radar, ultrasonic sensors, GPS, and speedometer.", "")
    add_p(doc, "(a) Healthcare: Disease diagnosis, AI radiology, and robotic surgery. (b) Autonomous Systems: Self-driving cars and delivery drones. (c) NLP & Finance: Large language models, algorithmic trading, and automated fraud detection.", "3. Future Scope & Applications:")

def page_2(doc):
    add_header_badge(doc, 2, "Unit 1: Intelligent Agents", "Winter 2025 (Q2.A) / Summer 2024 (Q1.C)")
    add_question_box(doc, "Explain in detail the structure of intelligent agents. Differentiate between Goal-Based Agents and Utility-Based Agents. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Every intelligent agent consists of hardware architecture and software control: Agent = Architecture + Program. The 5 architectures are Simple Reflex, Model-Based Reflex, Goal-Based, Utility-Based, and Learning Agents.", "1. General Agent Structure:")
    add_p(doc, "Combines current state with explicit Goal Information describing desirable outcomes. Evaluates future action consequences via search and planning algorithms. Flexible because changing the goal updates behavior dynamically without rewriting rules.", "2. Goal-Based Agents:")
    add_p(doc, "Employs an internal real-valued Utility Function U(s) -> R that measures the degree of success or 'happiness' in each reachable state. Selects actions that maximize Expected Utility under uncertainty: EU(a) = SUM [ P(s'|s,a) * U(s') ].", "3. Utility-Based Agents:")
    add_bullet(doc, "Goal Evaluation: Goal-based uses binary achievement (goal reached vs not reached); Utility-based measures continuous quality and degree of success.", "• Primary Differences:")
    add_bullet(doc, "Conflicting Objectives: Only Utility-based agents can balance trade-offs among conflicting goals (e.g., speed vs safety vs travel cost).", "")
    add_bullet(doc, "Environment Fit: Goal-based fits deterministic mazes; Utility-based fits complex, uncertain, stochastic real-world tasks.", "")

def page_3(doc):
    add_header_badge(doc, 3, "Unit 2: Problem-Solving & Search", "Winter 2025 (Q3.B) / Summer 2025 (Q3.A) / Summer 2024 (Q2.A)")
    add_question_box(doc, "Give the outline of Uniform Cost Search (UCS) algorithm with a suitable example. Discuss its completeness and optimality. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Uniform Cost Search (UCS) is an uninformed search algorithm that expands the node n with the lowest cumulative path cost g(n) using a Priority Queue. It is Dijkstra's algorithm generalized to search trees/graphs.", "1. Concept & Data Structure:")
    add_bullet(doc, "Initialize Frontier as Priority Queue ordered by g(n) with start node s0 (cost=0); Explored = empty set.", "Step 1:")
    add_bullet(doc, "If Frontier is empty, return Failure. Pop node n with lowest g(n) from Frontier.", "Step 2:")
    add_bullet(doc, "If GoalTest(n.state) == True, return Solution. (Goal test applied on expansion, NOT generation!)", "Step 3:")
    add_bullet(doc, "Add n.state to Explored. For each neighbor m, calculate path cost g(m) = g(n) + c(n, a, m).", "Step 4:")
    add_bullet(doc, "If m not in Explored or Frontier, insert it. If m in Frontier with higher cost, replace it with lower cost.", "Step 5:")
    add_p(doc, "Graph: Start S -> A (cost 1), S -> C (cost 2), S -> B (cost 5). C -> G (cost 4), A -> G (cost 9). UCS pops S, expands A(1) and C(2), then pops C and updates goal path to G with optimal cost 2+4 = 6 (avoiding expensive path A->G of cost 10).", "2. Worked Numerical Example:")
    add_p(doc, "Completeness: Guaranteed if step costs c >= eps > 0. Optimality: Yes, always finds cheapest path. Time & Space Complexity: O(b^(1 + floor(C*/eps))), where C* is optimal cost.", "3. Completeness & Optimality:")

def page_4(doc):
    add_header_badge(doc, 4, "Unit 2: Informed Search & Heuristics", "Summer 2024 (Q2.B) / Summer 2025 (Q1 MCQ)")
    add_question_box(doc, "Write the A* search algorithm and discuss the critical observations regarding admissibility, consistency, and over/underestimation of heuristics. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "A* search evaluates nodes using the evaluation function f(n) = g(n) + h(n), where g(n) is the exact cost from start to node n, and h(n) is the estimated heuristic cost from n to the nearest goal state.", "1. Evaluation Function:")
    add_bullet(doc, "Maintain OPEN (priority queue ordered by ascending f(n)) and CLOSED (explored nodes).", "Step 1:")
    add_bullet(doc, "Pop node n with lowest f(n) from OPEN. If GoalTest(n) == True, return Solution Path.", "Step 2:")
    add_bullet(doc, "Add n to CLOSED. For each successor m: calculate g(m) = g(n) + c(n,m) and f(m) = g(m) + h(m).", "Step 3:")
    add_bullet(doc, "If m not in OPEN or CLOSED, insert into OPEN. If already present with higher cost, update it.", "Step 4:")
    add_p(doc, "Admissibility: h(n) <= h*(n) (never overestimates). Guarantees tree-search optimality because suboptimal goals have f(G2) > C* >= f(n). Consistency: h(n) <= c(n,a,n') + h(n') (monotonicity). Guarantees graph optimality without reopening closed nodes.", "2. Admissibility & Consistency:")
    add_p(doc, "If h=0: f(n)=g(n), reduces to UCS (optimal, slow). If h < h* (underestimation): explores more nodes but 100% guarantees optimal path. If h > h* (overestimation): runs faster, but sacrifices optimality!", "3. Heuristic Observations:")

def page_5(doc):
    add_header_badge(doc, 5, "Unit 2: Adversarial Search", "Winter 2025 (Q3.A) / Summer 2025 (Q3.B)")
    add_question_box(doc, "What is Alpha-Beta pruning? Explain the function of alpha and beta, the cutoff conditions, and demonstrate with a game tree trace. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Alpha-Beta Pruning is an adversarial search optimization for 2-player zero-sum games. It prunes branches that cannot influence the final Minimax decision, returning the exact same optimal move while evaluating far fewer nodes.", "1. Concept & Equivalence:")
    add_p(doc, "Alpha (alpha): The best (highest) value MAX can guarantee so far along the path (initialized to -inf, updated at MAX nodes). Beta (beta): The best (lowest) value MIN can guarantee so far (initialized to +inf, updated at MIN nodes).", "2. Alpha and Beta Parameters:")
    add_p(doc, "Prune whenever alpha >= beta. (a) Alpha Cutoff (at MIN node): if value v <= alpha, prune remaining children because MAX will never pick this branch. (b) Beta Cutoff (at MAX node): if value v >= beta, prune remaining children because MIN above will never allow it.", "3. Cutoff Conditions:")
    add_p(doc, "Root A (MAX) has children B and C (MIN). Subtree under B evaluates leaf 3 and leaf 5, returning v=5 (beta=5). Sibling subtree under B sees leaf 6; since 6 >= beta(5), a Beta cutoff occurs, pruning its remaining leaf. C evaluates leaf 2; since beta(2) <= alpha(5), an Alpha cutoff occurs, pruning C's remaining subtree.", "4. Game Tree Trace:")
    add_p(doc, "Worst-case: O(b^m). Best-case (ideal move ordering): O(b^(m/2)). It searches twice as deep as standard Minimax in the same time!", "5. Efficiency:")

def page_6(doc):
    add_header_badge(doc, 6, "Unit 3: Knowledge Representation", "Winter 2025 (Q4.C) / Summer 2024 (Q3.A)")
    add_question_box(doc, "List and explain the fundamental issues in Knowledge Representation (KR). State the four major approaches to KR. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "(a) Relational: Entity-attribute tables (low reasoning). (b) Inheritable: Hierarchical trees (IS-A) where subclasses inherit parent properties. (c) Inferential: Formal mathematical logic (FOL) enabling deduction. (d) Procedural: Executable code and IF-THEN rules.", "1. Four Approaches to KR:")
    add_bullet(doc, "Important Attributes: Identifying universally relevant attributes (e.g., 'instance' and 'isa' drive classification and inheritance).", "1. Important Attributes:")
    add_bullet(doc, "Relationships Among Attributes: Modeling inverse relationships (e.g., ParentOf vs ChildOf), constraints, and dependencies between attributes.", "2. Relationship Modeling:")
    add_bullet(doc, "Granularity of Representation: Choosing primitive units (universal rules, but verbose facts) versus high-level concepts (compact facts, but coarse inference).", "3. Granularity:")
    add_bullet(doc, "Representing Sets of Objects: Distinguishing properties of the set itself (e.g., 'Elephants are endangered') from properties of individual members ('Elephants are gray').", "4. Set Representation:")
    add_bullet(doc, "Finding Right Structures (Indexing): Efficiently indexing and retrieving only the relevant sub-knowledge base from large repositories without exhaustive search.", "5. Indexing & Retrieval:")

def page_7(doc):
    add_header_badge(doc, 7, "Unit 3: First-Order Predicate Logic", "Winter 2025 (Q4.A) / Summer 2024 (Q3.B)")
    add_question_box(doc, "What is a Quantifier? Differentiate between Universal Quantifier (∀) and Existential Quantifier (∃) with suitable examples and duality rules. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "In First-Order Predicate Logic (FOL), a Quantifier expresses the scope and quantity of individuals in a domain of discourse that satisfy a given predicate expression.", "1. Definition of Quantifier:")
    add_p(doc, "Symbol: FORALL x P(x). Asserts that predicate P holds for EVERY object in the universe. Almost always paired with Implication (->). Example: 'All CSE students are smart' -> FORALL x (CSEStudent(x) -> Smart(x)).", "2. Universal Quantifier (FORALL):")
    add_p(doc, "Symbol: EXISTS x P(x). Asserts that predicate P holds for AT LEAST ONE object in the universe. Almost always paired with Conjunction (^). Example: 'Some cars are electric' -> EXISTS x (Car(x) ^ Electric(x)).", "3. Existential Quantifier (EXISTS):")
    add_bullet(doc, "~(FORALL x P(x)) == EXISTS x (~P(x)) ('Not everyone is rich' == 'Someone is not rich').", "• Duality Law 1:")
    add_bullet(doc, "~(EXISTS x P(x)) == FORALL x (~P(x)) ('Nobody is immortal' == 'Everyone is mortal').", "• Duality Law 2:")
    add_bullet(doc, "Same quantifiers commute: FORALL x FORALL y == FORALL y FORALL x. Mixed quantifiers DO NOT commute: FORALL x EXISTS y Loves(x,y) != EXISTS y FORALL x Loves(x,y).", "• Commutativity Rules:")

def page_8(doc):
    add_header_badge(doc, 8, "Unit 3: Rule-Based Reasoning", "Winter 2025 (Q4.B) / Summer 2025 (Q4.B/Q5.B) / Summer 2024 (Q3.C)")
    add_question_box(doc, "Differentiate between Forward and Backward Reasoning. Give the outline of the simple forward chaining algorithm with a suitable example. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Forward Reasoning (Data-Driven): Starts with known facts in Working Memory, matches rule premises, and fires rules to deduce new facts toward a goal. Used in synthesis, monitoring, and planning. Backward Reasoning (Goal-Driven): Starts with a goal hypothesis, searches for rules supporting it, and works backward to verify if facts exist. Used in medical diagnosis and debugging.", "1. Comparison:")
    add_bullet(doc, "Initialize Working Memory (WM) with given initial facts and load Rule Base.", "Step 1:")
    add_bullet(doc, "Match: Identify all rules whose premises are satisfied by current WM facts (Conflict Set).", "Step 2:")
    add_bullet(doc, "Conflict Resolution: Select highest-priority rule using specificity or recency strategy.", "Step 3:")
    add_bullet(doc, "Fire: Execute chosen rule; add its conclusion into Working Memory.", "Step 4:")
    add_bullet(doc, "Repeat Steps 2-4 until Goal is deduced in WM or no new rules match (Halts).", "Step 5:")
    add_p(doc, "Facts: F1: Croaks(Sam), F2: EatsFlies(Sam). Rules: R1: IF Croaks(x) ^ EatsFlies(x) THEN Frog(x). R2: IF Frog(x) THEN Green(x). Goal: Green(Sam). Cycle 1: F1 and F2 satisfy R1 premise -> Fire R1 -> Add Fact F3: Frog(Sam). Cycle 2: F3 satisfies R2 premise -> Fire R2 -> Add Fact F4: Green(Sam). Goal Reached!", "2. Worked Trace Example:")

def page_9(doc):
    add_header_badge(doc, 9, "Unit 4: Probabilistic Reasoning", "Winter 2025 (Q5.B) / Summer 2024 (Q4.B) / Summer 2025 (Q5.A)")
    add_question_box(doc, "Explain the Dempster-Shafer theory of evidence. Define Frame of Discernment, Mass function, Belief, Plausibility, and Dempster's Rule of Combination. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Dempster-Shafer (D-S) theory models uncertainty by allocating probability mass to subsets of hypotheses (power set 2^Theta) rather than atomic singletons, distinguishing between complete ignorance and equal probability.", "1. Motivation & Core Concept:")
    add_bullet(doc, "Frame of Discernment (Theta): Exhaustive set of mutually exclusive atomic hypotheses.", "• Frame of Discernment:")
    add_bullet(doc, "Basic Probability Assignment / Mass (m): m: 2^Theta -> [0, 1], where m(empty) = 0 and SUM [m(A)] = 1.", "• Mass Function m(A):")
    add_bullet(doc, "Belief Function Bel(A): Sum of masses of all subsets of A: Bel(A) = SUM_{B subset A} m(B) (lower bound).", "• Belief Bel(A):")
    add_bullet(doc, "Plausibility Function Pl(A): Sum of masses intersecting A: Pl(A) = 1 - Bel(~A) (upper bound).", "• Plausibility Pl(A):")
    add_bullet(doc, "Uncertainty Interval: [Bel(A), Pl(A)] quantifies the degree of ignorance regarding hypothesis A.", "• Uncertainty Interval:")
    add_p(doc, "Combines independent masses m1 and m2: m1,2(C) = [ SUM_{A intersect B = C} m1(A)*m2(B) ] / [ 1 - K ], where conflict factor K = SUM_{A intersect B = empty} m1(A)*m2(B). Normalization by (1 - K) redistributes conflicting mass.", "2. Dempster's Combination Rule:")

def page_10(doc):
    add_header_badge(doc, 10, "Unit 4: AI Planning", "Winter 2025 (Q5.A/C) / Summer 2025 (Q4.A) / Summer 2024 (Q4.C)")
    add_question_box(doc, "What is planning and why is it needed? List the components of a planning system and write the 4 STRIPS operators for the Block World problem. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Planning is the synthesis of an action sequence that transforms an initial state into a goal state. Needed because standard search suffers exponential state explosion; planning decomposes goals, isolates subproblems, and reasons bidirectionally.", "1. Definition & Need:")
    add_p(doc, "(a) State: Conjunction of ground literals (e.g., On(A, Table) ^ Clear(A)) under Closed World Assumption. (b) Goal: Conjunction of desired literals (partial state). (c) Action Schema: Operator Name, Preconditions, and Effects (Add and Delete Lists).", "2. Three Planning Components:")
    add_bullet(doc, "Pickup(x): Pre: Clear(x) ^ OnTable(x) ^ ArmEmpty; Add: Holding(x); Del: Clear(x), OnTable(x), ArmEmpty.", "1. Pickup(x):")
    add_bullet(doc, "Putdown(x): Pre: Holding(x); Add: Clear(x) ^ OnTable(x) ^ ArmEmpty; Del: Holding(x).", "2. Putdown(x):")
    add_bullet(doc, "Stack(x, y): Pre: Holding(x) ^ Clear(y); Add: On(x, y) ^ Clear(x) ^ ArmEmpty; Del: Holding(x), Clear(y).", "3. Stack(x, y):")
    add_bullet(doc, "Unstack(x, y): Pre: On(x, y) ^ Clear(x) ^ ArmEmpty; Add: Holding(x) ^ Clear(y); Del: On(x, y), Clear(x), ArmEmpty.", "4. Unstack(x, y):")
    add_p(doc, "Goal interaction where satisfying Goal 1 first clobbers Goal 2, requiring undoing work. Illustrates why linear planning fails and Non-Linear Planning is required.", "3. Sussman Anomaly:")

def page_11(doc):
    add_header_badge(doc, 11, "Unit 5: Natural Language Processing", "Winter 2025 (Q6.A/C) / Summer 2025 (Q6.A/C) / Summer 2024 (Q5.A/B)")
    add_question_box(doc, "Compare and contrast Syntactic Processing versus Semantic Processing in NLP. Explain the phases of NLP and the 4 major NLP ambiguities. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "Syntactic Processing verifies sentence structure against formal grammar (CFG) producing a parse tree. Semantic Processing extracts literal meaning and entity relationships producing a logical form. Benchmark: 'Colorless green ideas sleep furiously' is syntactically valid (NP + VP) but semantically absurd.", "1. Syntactic vs Semantic:")
    add_bullet(doc, "1. Lexical/Morphological: Tokenization, lemmatization, and POS tagging.", "• 5 Phases of NLP:")
    add_bullet(doc, "2. Syntactic Analysis: Parsing grammatical structures into parse trees.", "")
    add_bullet(doc, "3. Semantic Analysis: Extracting literal meaning and resolving word senses.", "")
    add_bullet(doc, "4. Discourse Integration: Resolving context across consecutive sentences (pronouns).", "")
    add_bullet(doc, "5. Pragmatic Analysis: Re-interpreting text using real-world commonsense and intent.", "")
    add_p(doc, "(a) Lexical: Word has multiple meanings ('river bank' vs 'money bank'). (b) Syntactic: Multiple parse trees ('I saw the man with binoculars'). (c) Referential: Ambiguous pronouns ('The trophy didn't fit in the suitcase because it was too big'). (d) Pragmatic: Speaker intent differs from text ('Can you pass the salt?').", "2. Four NLP Ambiguities:")

def page_12(doc):
    add_header_badge(doc, 12, "Unit 5: Expert Systems", "Winter 2025 (Q6.B) / Summer 2025 (Q6.B) / Summer 2024 (Q5.C)")
    add_question_box(doc, "What is an Expert System? With a neat sketch, explain the architecture, characteristic features, roles, and shells of an expert system. [6 Marks]")
    add_ans_header(doc)
    add_p(doc, "An Expert System is a knowledge-intensive AI program solving complex domain problems at human expert level. Key Features: Separation of knowledge from control, domain specificity, explanation capability ('Why' and 'How'), and heuristic reasoning under uncertainty.", "1. Definition & Features:")
    add_p(doc, "[User] <-> [User Interface] <-> [Inference Engine] <-> [Knowledge Base (Rules/Facts)]\n                                      |                     |\n                              [Working Memory]     [Explanation Facility]\n                                      |\n[Domain Expert] <-> [Knowledge Engineer] <-> [Knowledge Acquisition Module]", "2. Architecture Sketch:")
    add_bullet(doc, "Knowledge Base (KB): Storehouse of permanent domain facts and IF-THEN production rules.", "• 6 Core Modules:")
    add_bullet(doc, "Inference Engine: Processing unit matching facts against rules (Forward/Backward Chaining).", "")
    add_bullet(doc, "Working Memory: Dynamic storage of current session facts and intermediate deductions.", "")
    add_bullet(doc, "Explanation Facility: Transparency unit answering 'Why' a question is asked and 'How' concluded.", "")
    add_bullet(doc, "Knowledge Acquisition & UI: Authoring tools for engineers and friendly dialog for users.", "")
    add_p(doc, "Expert System Shell: An expert system without domain knowledge (Inference Engine + UI; e.g., EMYCIN, CLIPS). Landmark Applications: MYCIN (meningitis diagnosis), DENDRAL (molecular chemistry), PROSPECTOR (mineral discovery), XCON/R1 (VAX computer configuration).", "3. Shells & Applications:")

# ==================== MAIN EXECUTION ====================

def main():
    print("Creating PYQ Question-Answer Document with Font Size 14...")
    doc = create_doc()
    
    pages = [page_1, page_2, page_3, page_4, page_5, page_6, page_7, page_8, page_9, page_10, page_11, page_12]
    
    for i, p_func in enumerate(pages):
        print(f"Building Page {i+1}...")
        p_func(doc)
        if i < len(pages) - 1:
            doc.add_page_break()
            
    out_docx = "open-book-notes.docx"
    doc.save(out_docx)
    print(f"Successfully saved {out_docx} ({os.path.getsize(out_docx)} bytes)")

if __name__ == "__main__":
    main()
