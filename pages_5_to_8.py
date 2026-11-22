from docx_helpers import (
    add_page_header_banner, add_section_heading, add_subheading, 
    add_body_p, add_bullet_point, add_callout_box, create_table_grid, add_ascii_diagram
)
from docx.shared import Pt

def build_page_5(doc):
    # PAGE 5: Adversarial Search: Minimax & Alpha-Beta Pruning
    add_page_header_banner(doc, 5, "Unit 2: Adversarial Search", "Minimax Algorithm & Alpha-Beta Pruning")
    
    add_section_heading(doc, "1. Game Playing as Adversarial Search (Zero-Sum Games)")
    add_body_p(doc, 
        "In a 2-player, zero-sum, perfect information, deterministic game (e.g., Chess, Tic-Tac-Toe), two players (MAX and MIN) make alternate moves. "
        "A formal game has: (1) Initial State s0, (2) Player(s), (3) Actions(s), (4) Result(s, a), (5) TerminalTest(s), and (6) Utility(s, p). "
        "Zero-sum means MAX's gain is exactly equal to MIN's loss: Utility_MAX(s) + Utility_MIN(s) = 0.",
        "Formal Definition:")
    
    add_section_heading(doc, "2. Minimax Algorithm: Recursive Decision Engine")
    add_body_p(doc, 
        "MAX seeks moves that maximize final utility; MIN assumes worst-case and seeks moves that minimize MAX's utility. "
        "Minimax(s) = Utility(s) if Terminal(s); max_a Minimax(Result(s,a)) if Player(s)=MAX; min_a Minimax(Result(s,a)) if Player(s)=MIN. "
        "Complexity: Time O(b^m), Space O(bm) (Depth-first traversal). For Chess (b~35, m~80), Minimax is computationally intractable without pruning.",
        "Minimax Logic:")
    
    add_section_heading(doc, "3. Alpha-Beta Pruning Algorithm (Core PYQ Exam Topic)")
    add_body_p(doc, 
        "Alpha-Beta Pruning is an adversarial search optimization that prunes subtrees that cannot possibly influence the final decision. "
        "Crucially: Alpha-Beta returns the EXACT SAME optimal move as pure Minimax, but evaluates significantly fewer nodes.",
        "Definition & Equivalence:")
    
    headers_ab_def = ["Parameter", "Full Name", "Formal Definition & Operational Meaning", "Initial Value", "Updated By Node Type"]
    rows_ab_def = [
        ["alpha", "Alpha", "The best (highest/maximum) value that MAX can guarantee so far along the path to the current state.", "-Infinity", "Updated ONLY at MAX nodes: alpha = max(alpha, v)"],
        ["beta", "Beta", "The best (lowest/minimum) value that MIN can guarantee so far along the path to the current state.", "+Infinity", "Updated ONLY at MIN nodes: beta = min(beta, v)"]
    ]
    create_table_grid(doc, headers_ab_def, rows_ab_def, [0.8, 0.9, 3.4, 0.9, 1.47])
    
    add_subheading(doc, "Core Pruning Condition: alpha >= beta (Cutoff Criterion):")
    add_bullet_point(doc, "Occurs at a MIN node when current evaluated value v <= alpha. "
                          "Since MAX can already secure a value of alpha elsewhere on an earlier branch, MAX will NEVER choose the path leading to this MIN node. "
                          "Therefore, MIN's remaining sibling children can be safely PRUNED!", "Alpha Cutoff (at MIN node):")
    add_bullet_point(doc, "Occurs at a MAX node when current evaluated value v >= beta. "
                          "Since MIN above can already force a lower value of beta elsewhere, MIN will NEVER allow the game to reach this MAX node. "
                          "Therefore, MAX's remaining sibling children can be safely PRUNED!", "Beta Cutoff (at MAX node):")
    
    add_section_heading(doc, "4. Comprehensive Worked 4-Ply Game Tree Trace Example")
    add_ascii_diagram(doc, 
        "Level 0 (MAX):                 [ Root: A ]\n"
        "                              /           \\\n"
        "Level 1 (MIN):         [ B ]                 [ C ]\n"
        "                      /     \\               /     \\\n"
        "Level 2 (MAX):     [ D ]   [ E ]         [ F ]   [ G ]\n"
        "                   /   \\   /   \\         /   \\   /   \\\n"
        "Leaves:           3     5 6     9       1     2 0    -1\n"
        "                  (L1) (L2)(L3)(L4)    (L5) (L6)(L7) (L8)")
    
    headers_trace_ab = ["Node Evaluated", "Incoming [alpha, beta]", "Values Inspected", "Computed Node Value", "Updated [alpha, beta]", "Pruning Action / Status"]
    rows_trace_ab = [
        ["Node D (MAX)", "[-inf, +inf]", "Leaf 1 = 3, Leaf 2 = 5", "v = max(3, 5) = 5", "alpha = 5", "Full expansion; returns 5 to B"],
        ["Node B (MIN)", "[-inf, +inf]", "Child D = 5", "v = 5", "beta = 5", "[alpha=-inf, beta=5] passed down to E"],
        ["Node E (MAX)", "[-inf, 5]", "Leaf 3 = 6", "v = 6 >= beta (5)!", "alpha = max(-inf, 6)=6", "BETA CUTOFF AT E! alpha(6) >= beta(5). PRUNE Leaf 4 (9)!"],
        ["Node B Final", "[-inf, +inf]", "Child D=5, Child E=6", "v = min(5, 6) = 5", "Returns 5 to Root A", "Root A updates alpha = max(-inf, 5) = 5"],
        ["Node C (MIN)", "[5, +inf]", "Child F evaluated...", "---", "[alpha=5, beta=+inf]", "Root passes alpha=5 down to C"],
        ["Node F (MAX)", "[5, +inf]", "Leaf 5 = 1, Leaf 6 = 2", "v = max(1, 2) = 2", "alpha = 5", "Full expansion; returns 2 to C"],
        ["Node C Status", "[5, +inf]", "Child F returns 2", "v = min(+inf, 2) = 2", "beta = min(+inf, 2) = 2", "ALPHA CUTOFF AT C! beta(2) <= alpha(5). PRUNE Subtree G (Leaves 7, 8)!"]
    ]
    create_table_grid(doc, headers_trace_ab, rows_trace_ab, [1.1, 1.2, 1.4, 1.2, 1.2, 1.37])
    
    add_section_heading(doc, "5. Pruning Efficiency & Complexity Analysis")
    add_body_p(doc, 
        "In the worst case (adverse move ordering), Alpha-Beta visits all nodes, running in O(b^m). "
        "In the BEST CASE (perfect move ordering where best moves are examined first), time complexity drops to O(b^(m/2)) = O((sqrt(b))^m). "
        "This means Alpha-Beta can search TWICE AS DEEP as pure Minimax in the same amount of computation time!",
        "Complexity Gain:")

def build_page_6(doc):
    # PAGE 6: Knowledge Representation: Issues, Approaches & Propositional Logic
    add_page_header_banner(doc, 6, "Unit 3: Knowledge & Reasoning", "Knowledge Representation Issues, Approaches & Propositional Logic")
    
    add_section_heading(doc, "1. Foundations of Knowledge Representation (KR)")
    add_body_p(doc, 
        "Knowledge Representation is a formal language designed to express domain facts in computer-interpretable form so an inference engine can deduce new facts. "
        "KR bridges: (1) Real-World Facts <-> (2) Formal KR Representations. Reasoning corresponds to logical deduction: Facts -> (Representation) -> Internal Expressions -> (Deduction) -> New Expressions -> (Interpretation) -> New Real Facts.",
        "Representation & Mapping:")
    
    add_section_heading(doc, "2. Four Main Approaches to Knowledge Representation")
    headers_kr_app = ["Approach", "Core Representation Structure", "Inferential & Expressive Power", "Advantages & Disadvantages"]
    rows_kr_app = [
        ["Relational Knowledge", "Relational database tables: entities with attribute-value tuples.", "Weakest inferential power; relies on relational calculus/SQL joins.", "Simple, standardized, fast querying; cannot deduce novel implicit facts."],
        ["Inheritable Knowledge", "Hierarchical trees / Semantic networks with ISA and Instance links.", "Inheritance reasoning: subclasses inherit properties from parent classes.", "Natural taxonomy, property sharing; struggles with exceptions and multiple inheritance conflicts."],
        ["Inferential Knowledge", "Formal mathematical logic (Propositional and First-Order Predicate Logic).", "Highest inferential power: formal deduction via Modus Ponens and Resolution.", "Sound, complete, mathematically verified; computationally heavy and rigid."],
        ["Procedural Knowledge", "Executable code, functions, and IF-THEN production rules.", "High domain efficiency; encodes 'how-to' problem-solving control.", "Fast execution; hard to inspect, verify, modularize, or explain to users."]
    ]
    create_table_grid(doc, headers_kr_app, rows_kr_app, [1.4, 1.9, 2.0, 2.17])
    
    add_section_heading(doc, "3. Fundamental Issues in Knowledge Representation (Direct PYQ Answer)")
    headers_issues = ["KR Issue", "Detailed Core Problem", "Why It Matters in AI Systems", "Practical Technical Solution"]
    rows_issues = [
        ["1. Important Attributes", "Which attributes are fundamental across diverse domains?", "Determines structure of ontology; e.g., 'instance' and 'isa' attributes drive universal classification.", "Establish standard top-level foundational ontologies (Thing, Event, Agent)."],
        ["2. Relationships Among Attributes", "How to model inverse attributes, dependencies, and constraints?", "Attribute values constrain one another (e.g., ParentOf is inverse of ChildOf).", "Encode inverse relations, functional dependencies, and integrity constraints explicitly."],
        ["3. Granularity of Representation", "What level of detail should facts be stored at: High-level or Primitive?", "Primitive facts (e.g., John transferred object to Mary) allow universal inference rules but bloat facts. High-level is concise but lacks fine reasoning.", "Dual representation: store high-level predicates, expand into primitive decompositions only when necessary."],
        ["4. Representing Sets of Objects", "Distinguishing properties of the set as a whole vs properties of its members.", "E.g., 'Elephants are numerous' (property of the set) vs 'Elephants are gray' (property of individual members).", "Strict separation: treat sets as distinct meta-entities; use intensional vs extensional set definitions."],
        ["5. Finding Right Structures as Needed", "How to index and retrieve only the relevant subset of a massive KB during inference?", "Searching a million-fact KB blindly causes combinatorial explosion.", "Use semantic indexing, partitioned rule bases, Rete pattern-matching networks, and associative hashing."]
    ]
    create_table_grid(doc, headers_issues, rows_issues, [1.4, 2.2, 2.0, 1.87])
    
    add_section_heading(doc, "4. Propositional Logic (PL): Syntax, Truth Tables & Inference")
    add_body_p(doc, 
        "Propositional Logic models declarative statements that evaluate to either True or False. "
        "5 Connectives: Negation (NOT: ~P), Conjunction (AND: P ^ Q), Disjunction (OR: P v Q), Implication (IF-THEN: P -> Q == ~P v Q), Biconditional (IFF: P <-> Q).",
        "Syntax & Connectives:")
    
    headers_tt = ["P", "Q", "~P (NOT)", "P ^ Q (AND)", "P v Q (OR)", "P -> Q (Implication)", "P <-> Q (Biconditional)"]
    rows_tt = [
        ["False", "False", "True", "False", "False", "True", "True"],
        ["False", "True", "True", "False", "True", "True", "False"],
        ["True", "False", "False", "False", "True", "False", "False"],
        ["True", "True", "False", "True", "True", "True", "True"]
    ]
    create_table_grid(doc, headers_tt, rows_tt, [0.7, 0.7, 1.1, 1.2, 1.1, 1.4, 1.27])
    
    add_subheading(doc, "Representing Facts & Inference in Propositional Logic:")
    add_bullet_point(doc, "Fact 1: 'It is raining' -> P. Fact 2: 'If it rains, streets are wet' -> P -> Q. Fact 3: 'Streets are wet' -> Q.", "Representation:")
    add_bullet_point(doc, "Modus Ponens: From P and P -> Q, infer Q. Modus Tollens: From ~Q and P -> Q, infer ~P. Resolution: (A v B) ^ (~B v C) ==> (A v C).", "Inference Rules:")
    add_bullet_point(doc, "Propositional Logic cannot represent individual objects, properties, or quantifiers ('All students are smart' requires infinite propositions). This necessitates First-Order Predicate Logic!", "Inherent Limitation:")

def build_page_7(doc):
    # PAGE 7: First-Order Predicate Logic (FOL), Quantifiers & Rule-Based Reasoning
    add_page_header_banner(doc, 7, "Unit 3: Predicate Logic & Rules", "First-Order Logic (FOL), Quantifiers & Rule-Based Reasoning")
    
    add_section_heading(doc, "1. First-Order Predicate Logic (FOL): Foundations & Representation")
    add_body_p(doc, 
        "First-Order Logic overcomes Propositional Logic by modeling the world in terms of: "
        "(1) Objects (Constants: John, Lonere), (2) Relations/Predicates (Mortal(x), Likes(x, y)), (3) Functions (FatherOf(x)), and (4) Quantifiers (All, Some).",
        "Syntax:")
    add_bullet_point(doc, "Fact: 'Marcus was a Pompeian' -> Pompeian(Marcus) or Instance(Marcus, Pompeian).", "Instance Relationship:")
    add_bullet_point(doc, "Fact: 'All Pompeians were Romans' -> FORALL x (Pompeian(x) -> Roman(x)) or FORALL x (ISA(x, Pompeian) -> ISA(x, Roman)).", "ISA Relationship:")
    
    add_section_heading(doc, "2. Quantifiers: Universal (FORALL) vs Existential (EXISTS) — Master Differentiation")
    headers_quant = ["Comparison Dimension", "Universal Quantifier (FORALL / 'For All')", "Existential Quantifier (EXISTS / 'There Exists')", "Crucial Exam Caveat / Pitfall"]
    rows_quant = [
        ["Formal Symbol & Meaning", "Symbol: FORALL x P(x). True iff predicate P holds for EVERY object in domain.", "Symbol: EXISTS x P(x). True iff predicate P holds for AT LEAST ONE object in domain.", "Do not confuse scope: FORALL x EXISTS y != EXISTS y FORALL x."],
        ["Natural Connective Pairing", "ALMOST ALWAYS paired with Implication (->): FORALL x (Human(x) -> Mortal(x)).", "ALMOST ALWAYS paired with Conjunction (^): EXISTS x (Student(x) ^ LikesAI(x)).", "PITFALL: FORALL with ^ asserts everyone is a student; EXISTS with -> is trivially true if anyone isn't a student!"],
        ["De Morgan's Duality Laws", "~(FORALL x P(x)) == EXISTS x (~P(x)) ('Not everyone is rich' == 'Someone is not rich')", "~(EXISTS x P(x)) == FORALL x (~P(x)) ('Nobody is immortal' == 'Everyone is mortal')", "Negation flips quantifier type and pushes negation inside predicate."],
        ["Commutativity Rules", "FORALL x FORALL y P(x, y) == FORALL y FORALL x P(x, y) (Order does not matter).", "EXISTS x EXISTS y P(x, y) == EXISTS y EXISTS x P(x, y) (Order does not matter).", "CRITICAL: Mixing quantifiers is NOT commutative: FORALL x EXISTS y != EXISTS y FORALL x!"],
        ["Benchmark Translations", "'All CSE students pass': FORALL x (CSEStudent(x) -> Passes(x))", "'Some cars are electric': EXISTS x (Car(x) ^ Electric(x))", "'Everyone loves someone': FORALL x EXISTS y Loves(x, y) vs 'Someone is loved by all': EXISTS y FORALL x Loves(x, y)"]
    ]
    create_table_grid(doc, headers_quant, rows_quant, [1.4, 2.0, 2.0, 2.07])
    
    add_section_heading(doc, "3. Procedural vs Declarative Knowledge: Comprehensive Comparison")
    headers_p_vs_d = ["Comparison Feature", "Declarative Knowledge ('Knowing WHAT')", "Procedural Knowledge ('Knowing HOW')"]
    rows_p_vs_d = [
        ["Core Paradigm", "Explicit representation of facts, logic assertions, and relationships.", "Step-by-step algorithms, executable subroutines, and action procedures."],
        ["Separation of Knowledge & Control", "Complete separation: Knowledge Base is separate from Inference Engine.", "Intertwined: Knowledge and control flow are compiled together in code."],
        ["Ease of Verification & Modification", "Easy: Individual facts can be added, modified, or deleted independently.", "Difficult: Changing one procedure may have side effects across the system."],
        ["Computational Efficiency", "Lower: Requires general-purpose theorem proving / pattern matching.", "High: Direct execution of pre-compiled procedural operations."],
        ["Explanation Capability", "Natural: Generates clear audit trails of logical inference.", "Poor: Difficult to inspect runtime execution trace and answer 'Why'."],
        ["Exemplar Implementation", "Prolog, First-Order Logic facts, Semantic Web ontologies (OWL).", "LISP functions, Python scripts, hard-coded decision routines."]
    ]
    create_table_grid(doc, headers_p_vs_d, rows_p_vs_d, [1.6, 2.9, 2.97])
    
    add_section_heading(doc, "4. Forward Chaining vs Backward Chaining (With Simple Forward Algorithm)")
    add_body_p(doc, 
        "Forward Chaining (Data-Driven): Starts with known facts in Working Memory, matches rule premises, and fires rules to deduce new facts until goal is reached. "
        "Backward Chaining (Goal-Driven): Starts with a goal hypothesis, searches for rules whose conclusions match goal, and works backward to verify if premises hold in facts.",
        "Core Philosophy:")
    
    add_subheading(doc, "Simple Forward Chaining Algorithm Outline (Direct PYQ Answer):")
    add_bullet_point(doc, "Initialize Working Memory (WM) = Initial Known Facts; Rule Base = set of IF-THEN production rules.", "Step 1 (Initialization):")
    add_bullet_point(doc, "Match: Identify all rules whose premises are completely satisfied by current facts in WM (Conflict Set).", "Step 2 (Pattern Match):")
    add_bullet_point(doc, "Conflict Resolution: If Conflict Set has multiple rules, select one using a strategy (Priority, Specificity, Recency).", "Step 3 (Resolution):")
    add_bullet_point(doc, "Act/Fire: Execute chosen rule; add its conclusion to WM.", "Step 4 (Rule Firing):")
    add_bullet_point(doc, "Repeat Steps 2-4 until Goal is present in WM, or no new rules match (Halts).", "Step 5 (Termination):")
    
    add_subheading(doc, "Worked Trace Example:")
    add_body_p(doc, 
        "Initial Facts: F1: Croaks(Fritz), F2: EatsFlies(Fritz). Rules: R1: IF Croaks(x) ^ EatsFlies(x) THEN Frog(x). R2: IF Frog(x) THEN Green(x). Goal: Green(Fritz). "
        "Cycle 1: Match R1 with Fritz. F1 and F2 satisfy R1 premise. Fire R1 -> Add Fact F3: Frog(Fritz) to WM. "
        "Cycle 2: Match R2 with Fritz. F3 satisfies R2 premise. Fire R2 -> Add Fact F4: Green(Fritz) to WM. Goal reached!",
        "Step-by-Step Trace:")

def build_page_8(doc):
    # PAGE 8: Probabilistic Reasoning: Bayesian Networks & Dempster-Shafer Theory
    add_page_header_banner(doc, 8, "Unit 4: Probabilistic Reasoning", "Bayesian Networks & Dempster-Shafer Theory")
    
    add_section_heading(doc, "1. Reasoning Under Uncertainty & Bayes' Rule")
    add_body_p(doc, 
        "Classical logic fails in real-world environments due to theoretical ignorance (domain incomplete) and laziness (too many rules). "
        "Probability assigns a degree of belief between 0 and 1. Bayes' Rule updates hypothesis H given observed evidence E: "
        "P(H|E) = [ P(E|H) * P(H) ] / P(E) = [ P(E|H) * P(H) ] / [ P(E|H)P(H) + P(E|~H)P(~H) ].",
        "Foundations:")
    
    add_section_heading(doc, "2. Bayesian Networks (Belief Networks / Directed Acyclic Graphs)")
    add_body_p(doc, 
        "A Bayesian Network is a probabilistic graphical model representing conditional dependencies via a Directed Acyclic Graph (DAG): "
        "(1) Nodes represent random variables (discrete or continuous). (2) Directed Edges represent direct causal/probabilistic influences. "
        "(3) Each node Xi possesses a Conditional Probability Table (CPT) quantifying P(Xi | Parents(Xi)).",
        "Formal Definition:")
    
    add_subheading(doc, "Joint Probability Distribution Product Rule:")
    add_body_p(doc, 
        "A Bayesian Network compactly represents the full joint distribution using the factorization: "
        "P(X1, X2, ..., Xn) = PRODUCT_i=1..n [ P(Xi | Parents(Xi)) ]. This reduces exponential parameter complexity from O(2^n) to linear in network structure.",
        "Master Equation:")
    
    add_ascii_diagram(doc, 
        "Classic Burglary-Alarm Network:\n"
        "      [ Burglary (B) ]       [ Earthquake (E) ]\n"
        "             \\                     /\n"
        "              v                   v\n"
        "                 [ Alarm (A) ]\n"
        "                 /           \\\n"
        "                v             v\n"
        "        [ JohnCalls (J) ]    [ MaryCalls (M) ]")
    
    add_subheading(doc, "Numerical Query Trace (Burglary Network):")
    add_body_p(doc, 
        "Calculate P(B ^ ~E ^ A ^ J ^ ~M): "
        "By DAG factorization: P(B ^ ~E ^ A ^ J ^ ~M) = P(B) * P(~E) * P(A | B ^ ~E) * P(J | A) * P(~M | A). "
        "Given CPT values: P(B) = 0.001, P(~E) = 0.998, P(A | B ^ ~E) = 0.94, P(J | A) = 0.90, P(~M | A) = 1 - 0.70 = 0.30. "
        "Calculation: 0.001 * 0.998 * 0.94 * 0.90 * 0.30 = 0.00025286 (0.0253%).",
        "Step-by-Step Calculation:")
    
    add_section_heading(doc, "3. Dempster-Shafer (D-S) Theory of Evidence (Direct PYQ Answer)")
    add_body_p(doc, 
        "Dempster-Shafer theory models degrees of belief without requiring probabilities for all individual states. "
        "Unlike Bayesian probability, D-S theory distinguishes between complete ignorance (no evidence) and equal probability (coin toss). "
        "It assigns probability mass to subsets of hypotheses (power set) rather than atomic singletons.",
        "Motivation & Philosophy:")
    
    headers_ds = ["D-S Mathematical Concept", "Formal Formula / Definition", "Operational Meaning & Function in AI"]
    rows_ds = [
        ["Frame of Discernment (Theta)", "Theta = {theta1, theta2, ..., thetan}", "Exhaustive set of mutually exclusive atomic hypotheses. Power set 2^Theta contains all subsets."],
        ["Basic Probability Assignment (m)", "m: 2^Theta -> [0, 1], where m(empty) = 0, SUM [m(A)] = 1", "Mass function allocating belief to set A that cannot be further divided among sub-hypotheses."],
        ["Belief Function Bel(A)", "Bel(A) = SUM_{B subset_of A} [ m(B) ]", "Total lower-bound belief: sum of all masses directly supporting subsets of A (Conservative support)."],
        ["Plausibility Function Pl(A)", "Pl(A) = SUM_{B intersect A != empty} [ m(B) ] = 1 - Bel(~A)", "Total upper-bound belief: sum of all masses not actively contradicting A (Optimistic support)."],
        ["Uncertainty Interval", "Interval = [Bel(A), Pl(A)]", "Width [Pl(A) - Bel(A)] quantifies degree of ignorance regarding hypothesis A."]
    ]
    create_table_grid(doc, headers_ds, rows_ds, [1.5, 2.4, 3.57])
    
    add_section_heading(doc, "4. Dempster's Rule of Combination (Orthogonal Sum)")
    add_body_p(doc, 
        "Combines two independent mass functions m1 and m2 over identical Frame of Discernment Theta: "
        "m1,2(C) = [ SUM_{A intersect B = C} m1(A)*m2(B) ] / [ 1 - K ], where conflict factor K = SUM_{A intersect B = empty} m1(A)*m2(B).",
        "Combination Formula:")
    
    add_subheading(doc, "Numerical Trace (Medical Diagnosis Example):")
    add_body_p(doc, 
        "Frame Theta = {Flu (F), Cold (C)}. Doctor 1 assigns: m1({F}) = 0.6, m1(Theta) = 0.4. Doctor 2 assigns: m2({C}) = 0.7, m2(Theta) = 0.3. "
        "Matrix of Products: "
        "(1) {F} intersect {C} = empty -> Product = 0.6 * 0.7 = 0.42 (Conflict!). "
        "(2) {F} intersect Theta = {F} -> Product = 0.6 * 0.3 = 0.18. "
        "(3) Theta intersect {C} = {C} -> Product = 0.4 * 0.7 = 0.28. "
        "(4) Theta intersect Theta = Theta -> Product = 0.4 * 0.3 = 0.12. "
        "Conflict Factor K = 0.42. Normalization denominator = 1 - K = 1 - 0.42 = 0.58. "
        "Combined Masses: m1,2({F}) = 0.18 / 0.58 = 0.310 (31.0%). m1,2({C}) = 0.28 / 0.58 = 0.483 (48.3%). m1,2(Theta) = 0.12 / 0.58 = 0.207 (20.7%).",
        "Step-by-Step Calculation:")
