from docx_helpers import (
    add_page_header_banner, add_section_heading, add_subheading, 
    add_body_p, add_bullet_point, add_callout_box, create_table_grid, add_ascii_diagram
)
from docx.shared import Pt

def build_page_9(doc):
    # PAGE 9: Fuzzy Sets & AI Planning (STRIPS Block World)
    add_page_header_banner(doc, 9, "Unit 4: Fuzzy Logic & Planning", "Fuzzy Sets, Membership Functions & AI Planning (STRIPS)")
    
    add_section_heading(doc, "1. Fuzzy Sets, Degree of Membership & Computer Representation")
    add_body_p(doc, 
        "In classical (Crisp) set theory, an element either belongs or does not belong: mu_A(x) in {0, 1}. "
        "In Fuzzy Set theory (Lotfi Zadeh, 1965), membership is gradual, taking continuous truth values in the real interval [0, 1]. "
        "Membership function mu_A(x) defines the degree of truth with which element x belongs to fuzzy set A.",
        "Crisp vs Fuzzy:")
    
    headers_fuz = ["Fuzzy Region / Concept", "Mathematical Definition", "Operational Meaning in AI Systems"]
    rows_fuz = [
        ["Core of Fuzzy Set A", "Core(A) = {x in X | mu_A(x) = 1.0}", "Set of all points that are completely, unambiguously members of fuzzy set A."],
        ["Support of Fuzzy Set A", "Support(A) = {x in X | mu_A(x) > 0.0}", "Set of all points that have non-zero membership in fuzzy set A."],
        ["Boundary of Fuzzy Set A", "Boundary(A) = {x in X | 0.0 < mu_A(x) < 1.0}", "Region of vagueness/uncertainty where membership is partial."],
        ["Discrete Computer Representation", "A = { (x1, mu_A(x1)), (x2, mu_A(x2)), ... }", "Represented as arrays/vectors of key-value pairs or lookup tables."],
        ["Continuous Computer Representation", "Triangular (a, b, c), Trapezoidal (a, b, c, d)", "Stored concisely as 3 or 4 geometric coordinate parameters."]
    ]
    create_table_grid(doc, headers_fuz, rows_fuz, [1.6, 2.4, 3.47])
    
    add_subheading(doc, "Fuzzy Set Mathematical Operations:")
    add_bullet_point(doc, "mu_{A union B}(x) = max(mu_A(x), mu_B(x)). E.g., max(0.8, 0.4) = 0.8.", "Fuzzy Union (OR):")
    add_bullet_point(doc, "mu_{A intersect B}(x) = min(mu_A(x), mu_B(x)). E.g., min(0.8, 0.4) = 0.4.", "Fuzzy Intersection (AND):")
    add_bullet_point(doc, "mu_{NOT A}(x) = 1 - mu_A(x). E.g., 1 - 0.7 = 0.3.", "Fuzzy Complement (NOT):")
    
    add_section_heading(doc, "2. AI Planning Systems: Overview, Need & Core Components")
    add_body_p(doc, 
        "Planning is the task of finding a sequence of actions that achieves a goal, starting from an initial state. "
        "Why Planning is needed over standard Search: Standard search searches state space blindly or with heuristic estimates on atomic states; "
        "planning systems represent states and actions symmetrically with logic literals, allowing goals to be decomposed into independent subgoals, "
        "enabling backward search from goals, and avoiding combinatorial state explosion.",
        "Definition & Need:")
    
    headers_plan_comp = ["Planning Component", "Formal Representation Structure", "Function in Classical Planning System"]
    rows_plan_comp = [
        ["State Representation", "Conjunction of positive function-free ground literals (e.g., On(A, Table) ^ Clear(A)).", "Complete description of current world under Closed World Assumption (unmentioned literals are False)."],
        ["Goal Representation", "Conjunction of desired literals (e.g., On(A, B) ^ On(B, C)).", "Specifies partial state conditions that must be True in final goal state."],
        ["Action / Operator Representation", "Operator(Name, Parameters, Preconditions, Effects: Add List, Delete List)", "Defines action applicability (Preconditions) and state changes (Effects: Add/Delete)."]
    ]
    create_table_grid(doc, headers_plan_comp, rows_plan_comp, [1.5, 2.5, 3.47])
    
    add_section_heading(doc, "3. Planning Terminologies & Goal Stack Planning (GSP)")
    add_body_p(doc, 
        "Goal Stack Planning maintains a stack of subgoals, composite goals, and operators. It decomposes compound goals and solves them sequentially.",
        "Mechanism:")
    add_bullet_point(doc, "STRIPS Assumption: Literals not explicitly mentioned in an operator's Add or Delete lists remain completely unchanged by the action.", "STRIPS Assumption:")
    add_bullet_point(doc, "Clobbering / Threat: An operator in the plan deletes a precondition required by a subsequent step (causes goal interactions).", "Clobberer:")
    
    add_subheading(doc, "The 4 STRIPS Operators for Block World Problem (Direct PYQ Answer):")
    headers_bw = ["Operator Name", "Preconditions (Must hold before action)", "Add List (Added to state)", "Delete List (Removed from state)"]
    rows_bw = [
        ["Pickup(x)", "Clear(x) ^ OnTable(x) ^ ArmEmpty", "Holding(x)", "Clear(x), OnTable(x), ArmEmpty"],
        ["Putdown(x)", "Holding(x)", "OnTable(x) ^ Clear(x) ^ ArmEmpty", "Holding(x)"],
        ["Stack(x, y)", "Holding(x) ^ Clear(y)", "On(x, y) ^ Clear(x) ^ ArmEmpty", "Holding(x), Clear(y)"],
        ["Unstack(x, y)", "On(x, y) ^ Clear(x) ^ ArmEmpty", "Holding(x) ^ Clear(y)", "On(x, y), Clear(x), ArmEmpty"]
    ]
    create_table_grid(doc, headers_bw, rows_bw, [1.1, 2.3, 2.1, 1.97])
    
    add_subheading(doc, "The Sussman Anomaly (Goal Interaction Challenge):")
    add_body_p(doc, 
        "In Block World, when Goal = On(A, B) ^ On(B, C), linear Goal Stack Planning fails: achieving On(A, B) first requires unstacking it later to achieve On(B, C), "
        "and achieving On(B, C) first clobbers On(A, B). This proves that linear sequential planning is incomplete and necessitates Non-Linear / Partial Order Planning (POP).",
        "Sussman Anomaly:")

def build_page_10(doc):
    # PAGE 10: Natural Language Processing & Syntactic vs Semantic Processing
    add_page_header_banner(doc, 10, "Unit 5: NLP", "Natural Language Processing & Syntactic vs Semantic Processing")
    
    add_section_heading(doc, "1. Natural Language Processing (NLP): Scope & Core Subfields")
    add_body_p(doc, 
        "Natural Language Processing (NLP) is the subfield of AI enabling machines to understand, interpret, and generate human languages. "
        "NLP encompasses two core operational subfields: "
        "(1) Natural Language Understanding (NLU): Comprehending text/speech by converting surface strings into deep unambiguous semantic representations. "
        "(2) Natural Language Generation (NLG): Converting structured internal computer concepts into coherent, grammatically fluent human sentences.",
        "Foundations:")
    
    add_section_heading(doc, "2. Five/Six Phases of the NLP Pipeline (With Flow Diagram)")
    add_ascii_diagram(doc, 
        "[Raw Text Input] ---> [Phase 1: Morphological/Lexical Analysis] ---> Tokens & POS Tags\n"
        "                                           |\n"
        "                                           v\n"
        "                      [Phase 2: Syntactic Analysis (Parsing)]   ---> Parse Trees (CFG)\n"
        "                                           |\n"
        "                                           v\n"
        "                      [Phase 3: Semantic Analysis]             ---> Logical Meaning\n"
        "                                           |\n"
        "                                           v\n"
        "                      [Phase 4: Discourse Integration]         ---> Cross-Sentence Context\n"
        "                                           |\n"
        "                                           v\n"
        "                      [Phase 5: Pragmatic Analysis]            ---> Real-World Intent/Action")
    
    headers_phases = ["NLP Phase", "Core Transformation / Operation", "Key Algorithms / Tools", "Example Error Detected / Solved"]
    rows_phases = [
        ["1. Lexical / Morphological", "Tokenization, lemmatization, stemming, prefix/suffix stripping, POS tagging.", "Byte-Pair Encoding, WordNet, Porter Stemmer", "Distinguishes 'running' (verb) vs 'running' (noun)."],
        ["2. Syntactic Analysis", "Validates sentence grammatical structure against formal grammar (CFG); generates parse tree.", "Top-Down, Bottom-Up, CYK, Earley Parser", "Flags syntax error in: 'Boy the ball kicked'."],
        ["3. Semantic Analysis", "Translates parse trees into unambiguous meaning representation; checks semantic sense.", "Case Grammar, Semantic Role Labeling (SRL)", "Rejects absurdity: 'The hot ice-cream froze the sun'."],
        ["4. Discourse Integration", "Resolves meaning across multiple consecutive sentences; resolves pronoun references.", "Centering Theory, Anaphora/Cataphora resolution", "Resolves 'it': 'I dropped the glass on table; it broke'."],
        ["5. Pragmatic Analysis", "Interprets text using real-world commonsense, situational context, intent, sarcasm.", "Speech Act Theory, Gricean Maxims, World Knowledge", "Interprets: 'Can you pass the salt?' as request, not ability."]
    ]
    create_table_grid(doc, headers_phases, rows_phases, [1.4, 2.4, 1.8, 1.87])
    
    add_section_heading(doc, "3. Syntactic Processing vs Semantic Processing (Master PYQ Comparison Table)")
    headers_syn_sem = ["Comparison Dimension", "Syntactic Processing ('Grammar')", "Semantic Processing ('Meaning')"]
    rows_syn_sem = [
        ["Primary Objective", "Determine whether sentence follows formal grammatical rules of language.", "Extract literal, unambiguous meaning and relationships between entities."],
        ["Input & Output", "Input: Sequence of lexical tokens. Output: Syntactic Parse Tree.", "Input: Parse Tree + Lexicon. Output: Logical Form / Conceptual Graph."],
        ["Knowledge Base Utilized", "Formal Grammar rules: Context-Free Grammars (CFG), syntax phrase structures.", "Domain Ontologies, semantic lexicons (WordNet), Case frames, World knowledge."],
        ["Ambiguity Addressed", "Structural & attachment ambiguity (e.g., prepositional phrase attachment).", "Word Sense Ambiguity (Polysemy: bank as river vs financial institution)."],
        ["Classic Test Case", "Accepts: 'Colorless green ideas sleep furiously' as grammatically valid (NP + VP).", "Rejects: 'Colorless green ideas sleep furiously' as semantically meaningless."],
        ["Typical Algorithms", "Context-Free Parsers: CYK, Earley algorithm, Chart parsing, Shift-Reduce.", "Selectional Restrictions, Case Grammar (Fillmore), Semantic Role Labeling."],
        ["Dependency on Context", "Largely local: checks sentence-level token arrangements.", "Global: requires word senses, entity types, and conceptual dependencies."]
    ]
    create_table_grid(doc, headers_syn_sem, rows_syn_sem, [1.5, 2.9, 3.07])
    
    add_section_heading(doc, "4. Semantic Analysis & The 4 Core NLP Ambiguities")
    add_bullet_point(doc, "Lexical Ambiguity: Single word has multiple dictionary meanings. E.g., 'She went to the bank'. Solved by: Word Sense Disambiguation (WSD), Lesk Algorithm.", "1. Lexical Ambiguity:")
    add_bullet_point(doc, "Syntactic Ambiguity: Sentence has multiple legal parse trees. E.g., 'I saw the man with binoculars'. Solved by: Probabilistic CFG (PCFG).", "2. Syntactic Ambiguity:")
    add_bullet_point(doc, "Referential / Anaphoric Ambiguity: Pronoun reference is unclear. E.g., 'The monkey ate the banana because it was hungry/ripe'. Solved by: Commonsense Knowledge.", "3. Referential Ambiguity:")
    add_bullet_point(doc, "Pragmatic Ambiguity: Literal meaning differs from speaker intent. E.g., 'Do you know what time it is?'. Solved by: Pragmatic Speech Act Theory.", "4. Pragmatic Ambiguity:")

def build_page_11(doc):
    # PAGE 11: Expert Systems: Architecture, Shells, Roles & Applications
    add_page_header_banner(doc, 11, "Unit 5: Expert Systems", "Expert Systems — Architecture, Characteristic Features, Roles & Shells")
    
    add_section_heading(doc, "1. Definition & Characteristic Features of Expert Systems")
    add_body_p(doc, 
        "An Expert System is a knowledge-intensive artificial intelligence software program that captures human domain expertise "
        "and solves complex problems within a specialized domain at the level of a human specialist (Feigenbaum).",
        "Definition:")
    
    headers_es_feat = ["Characteristic Feature", "Technical Description", "Why It Sets Expert Systems Apart from Standard Code"]
    rows_es_feat = [
        ["1. Separation of Knowledge & Control", "Domain knowledge (Knowledge Base) is completely decoupled from execution engine (Inference Engine).", "Enables updating medical/legal rules without modifying or recompiling the underlying program."],
        ["2. Domain Specificity & High Performance", "Possesses deep heuristic knowledge in a narrow specialized vertical rather than shallow general knowledge.", "Solves complex problems (e.g., infectious disease diagnosis) with accuracy rivaling human experts."],
        ["3. Symbolic & Heuristic Reasoning", "Employs symbolic representations and experiential 'rules of thumb' rather than purely numerical algorithms.", "Handles incomplete, uncertain, and heuristic real-world problem scenarios."],
        ["4. Explanation Capability (Transparency)", "Explains 'WHY' a question is asked and 'HOW' a conclusion was reached (complete audit trail).", "Essential for high-stakes medical, legal, and financial domains where black-box decisions are unacceptable."],
        ["5. Handling Uncertainty", "Integrates Certainty Factors (CF), Dempster-Shafer theory, or Fuzzy logic into rule evaluations.", "Makes reliable recommendations even when patient symptoms or sensor readings are missing or fuzzy."]
    ]
    create_table_grid(doc, headers_es_feat, rows_es_feat, [1.5, 2.7, 3.27])
    
    add_section_heading(doc, "2. Architecture of an Expert System (Neat Sketch & Core Modules)")
    add_ascii_diagram(doc, 
        "                  +----------------------------------------------+\n"
        "                  |              EXPERT SYSTEM                   |\n"
        "                  |  +----------------------------------------+  |\n"
        "                  |  |             USER INTERFACE             |  |\n"
        "                  |  +--------------------+-------------------+  |\n"
        "                  |                       |                      |\n"
        "                  |                       v                      |\n"
        "                  |  +----------------------------------------+  |\n"
        "                  |  |            INFERENCE ENGINE            |  |\n"
        "                  |  |  (Forward Chaining / Backward Chaining)|  |\n"
        "                  |  +----------+-------------------+---------+  |\n"
        "                  |             |                   |            |\n"
        "                  |             v                   v            |\n"
        "                  |  +--------------------+  +----------------+  |\n"
        "                  |  |   KNOWLEDGE BASE   |  | WORKING MEMORY |  |\n"
        "                  |  | (IF-THEN Rules,    |  | (Current Case  |  |\n"
        "                  |  |  Static Domain     |  |  Facts, Goals, |  |\n"
        "                  |  |  Ontologies)       |  |  Intermediate) |  |\n"
        "                  |  +----------+---------+  +----------------+  |\n"
        "                  |             ^                   ^            |\n"
        "                  |             |                   |            |\n"
        "                  |  +----------+-------------------+---------+  |\n"
        "                  |  |          EXPLANATION FACILITY          |  |\n"
        "                  |  |           ('Why' and 'How')            |  |\n"
        "                  |  +----------------------------------------+  |\n"
        "                  |  +----------------------------------------+  |\n"
        "                  |  |      KNOWLEDGE ACQUISITION MODULE      |  |\n"
        "                  |  +--------------------+-------------------+  |\n"
        "                  +-----------------------|----------------------+\n"
        "                                          v\n"
        "                     [Knowledge Engineer] <---> [Domain Expert]")
    
    add_subheading(doc, "The 6 Core Modules of Expert System Architecture:")
    add_bullet_point(doc, "Knowledge Base (KB): Repository of domain rules (IF condition THEN action) and permanent static facts.", "1. Knowledge Base:")
    add_bullet_point(doc, "Inference Engine: Processing unit that selects rules from KB and applies Forward/Backward Chaining against current facts.", "2. Inference Engine:")
    add_bullet_point(doc, "Working Memory (Fact Base): Dynamic storage for session-specific facts, patient data, and intermediate deductions.", "3. Working Memory:")
    add_bullet_point(doc, "Explanation Facility: Provides transparency by answering: 'WHY is this test needed?' and 'HOW was disease diagnosed?'.", "4. Explanation Facility:")
    add_bullet_point(doc, "Knowledge Acquisition Module: Authoring subsystem allowing Knowledge Engineers to translate expert heuristics into formal rules.", "5. Knowledge Acquisition:")
    add_bullet_point(doc, "User Interface: Natural language dialog / GUI through which non-expert users input case data and view recommendations.", "6. User Interface:")
    
    add_section_heading(doc, "3. Expert System Shells, Roles & Landmark Applications")
    add_body_p(doc, 
        "An Expert System Shell is an expert system stripped of its domain-specific knowledge base (Shell = Inference Engine + Explanation Facility + UI). "
        "Engineers plug in a new Knowledge Base to create a new system rapidly without re-engineering the inference engine. Examples: EMYCIN, CLIPS, JESS.",
        "Expert System Shells:")
    
    headers_apps = ["Landmark System", "Specialized Domain", "Inference Paradigm / Shell", "Historic Impact & Real-World Role"]
    rows_apps = [
        ["MYCIN (Stanford, 1970s)", "Medical diagnosis of bacterial blood infections (meningitis).", "Backward Chaining with Certainty Factors (EMYCIN).", "Prescribed antibiotic therapies; outperformed junior physicians; pioneered explanation."],
        ["DENDRAL (Stanford, 1965)", "Chemical mass spectrometry molecular structure analysis.", "Plan-Generate-and-Test with heuristic constraints.", "First successful knowledge-based system; proved 'knowledge is power'."],
        ["PROSPECTOR (SRI, 1978)", "Mineral exploration and geological site evaluation.", "Rule-based Bayesian inference networks.", "Accurately predicted a major molybdenum deposit worth over $100 Million."],
        ["XCON / R1 (DEC, 1980)", "Automated hardware configuration of VAX computer systems.", "Forward Chaining (OPS5 rule language).", "Saved Digital Equipment Corporation (DEC) an estimated $40 Million annually."]
    ]
    create_table_grid(doc, headers_apps, rows_apps, [1.4, 2.0, 1.8, 2.27])

def build_page_12(doc):
    # PAGE 12: Comprehensive Master Objective & MCQ Question Bank (Solved)
    add_page_header_banner(doc, 12, "Compulsory Q1 Bank", "Comprehensive Master Objective & MCQ Question Bank (Solved)")
    
    add_section_heading(doc, "1. Solved Objective & MCQ Bank (From DBATU Regular & Supplementary Papers)")
    add_body_p(doc, 
        "The following 25 MCQs are curated directly from DBATU Sem-7 AI examination papers (Winter 2025 Regular, Summer 2025 Supply, "
        "and Summer 2024 Supplementary). Each item includes the verified correct answer and a crisp 1-line exam rationale.",
        "Compulsory Section Q1 Preparation:")
    
    headers_mcq = ["No.", "Question Prompt & Syllabus Unit", "Correct Answer Option", "Concise 1-Line Conceptual Rationale"]
    rows_mcq = [
        ["1", "Primary goal of Artificial Intelligence (AI)?", "B) Machines that think and act rationally", "Rational action is the modern paradigm; replaces human imitation."],
        ["2", "Which best describes an intelligent agent?", "B) Perceives environment and takes actions", "Formal definition: Agent = Sensor percept mapping to actuator actions."],
        ["3", "Which environment is easiest for AI agent?", "A) Fully observable and deterministic", "No hidden state to remember; next state is 100% predictable."],
        ["4", "Search expanding level-by-level without path cost?", "C) Breadth-First Search (BFS)", "BFS uses FIFO queue to explore state space strictly level by level."],
        ["5", "What is state space?", "D) Representing problem with variable & parameters", "State space defines all possible valid problem configurations."],
        ["6", "Example of a heuristic function in AI?", "B) Manhattan distance in a grid problem", "Estimates remaining distance without obstacle computation."],
        ["7", "Knowledge/reasoning crucial role in dealing with?", "B) Partially Observable environment", "Inference deduces unobserved states from percept histories."],
        ["8", "Reasoning working backward from goal?", "B) Backward reasoning / chaining", "Goal-driven reasoning matching rule consequences back to facts."],
        ["9", "Primary purpose of Bayesian networks?", "B) To handle reasoning under uncertainty", "Compactly models joint probability distributions via DAG CPTs."],
        ["10", "Semantic analysis in NLP focuses on?", "C) Extracting meaning from text", "Distinguishes literal meaning from pure grammatical syntax."],
        ["11", "Which is NOT a standard connective in FOL?", "B) iff (or non-standard connective)", "Standard connectives are: NOT (~), AND (^), OR (v), Implication (->)."],
        ["12", "Where does Bayes rule can be used?", "D) Answering probabilistic queries", "Updates belief in hypothesis given observed sensor evidence."],
        ["13", "Factor fundamentally limiting rational agent?", "A) Infinite computational resources", "Bounded rationality is required because real agents have finite CPU/RAM."],
        ["14", "Rationality of an agent depends on?", "c) Performance, percept sequence, knowledge, actions", "Formal definition: 4-tuple PEAS dependency of rationality."],
        ["15", "A heuristic function h(n) is admissible if?", "c) Never overestimates actual cost to goal", "Condition h(n) <= h*(n) guarantees optimality of A* tree search."],
        ["16", "Alpha-Beta pruning is primarily used in?", "c) Game-playing adversarial search", "Prunes Minimax game tree branches that cannot affect outcome."],
        ["17", "Key advantage of predicate logic over propositional?", "b) Ability to express relationships between objects", "Adds variables, predicates, and quantifiers (FORALL, EXISTS)."],
        ["18", "Procedural knowledge is typically harder to?", "c) Explain / verify", "Intertwines control and logic, making explanation facilities brittle."],
        ["19", "Bayesian networks model uncertainty through?", "a) Conditional probability distributions", "Each DAG node stores a Conditional Probability Table (CPT)."],
        ["20", "Learning from a set of pre-classified examples?", "c) Inductive / Supervised Learning", "Extracts generalized rules from labeled input-output instances."],
        ["21", "Expert systems differ from standard AI because?", "c) Capture human domain knowledge in rules", "Strict separation of Knowledge Base from Inference Engine."],
        ["22", "A neural network's weights are best described as?", "b) Adjustable parameters encoding knowledge", "Learned knowledge is stored numerically in connection synaptic weights."],
        ["23", "Search strategy most susceptible to local optima?", "a) Hill Climbing", "Greedy local search lacks backtrack; halts at local peaks."],
        ["24", "Evaluation function in A* search?", "f(n) = g(n) + h(n)", "g(n) is exact cost incurred; h(n) is estimated cost to goal."],
        ["25", "STRIPS assumption dictates that?", "Literals unmentioned in effects remain unchanged", "Avoids the Frame Problem in classical action representation."]
    ]
    create_table_grid(doc, headers_mcq, rows_mcq, [0.4, 2.2, 2.0, 2.87])
    
    add_section_heading(doc, "2. Master Search Complexity & Logic Cheat Matrix (Exam Quick Reference)")
    headers_cheat = ["Algorithm", "Frontier Data Structure", "Time Complexity", "Space Complexity", "Complete?", "Optimal?"]
    rows_cheat = [
        ["Breadth-First Search (BFS)", "FIFO Queue", "O(b^d)", "O(b^d)", "Yes (if b is finite)", "Yes (if step costs equal)"],
        ["Depth-First Search (DFS)", "LIFO Stack", "O(b^m)", "O(b * m)", "No (infinite paths)", "No"],
        ["Uniform Cost Search (UCS)", "Priority Queue [g(n)]", "O(b^(1+floor(C*/eps)))", "O(b^(1+floor(C*/eps)))", "Yes (if cost >= eps > 0)", "Yes (always optimal)"],
        ["Greedy Best-First Search", "Priority Queue [h(n)]", "O(b^m)", "O(b^m)", "No (can loop)", "No"],
        ["A* Search Algorithm", "Priority Queue [g(n)+h(n)]", "O(b^d)", "O(b^d)", "Yes (if cost >= eps)", "Yes (if h admissible/consistent)"],
        ["Minimax Game Search", "Recursive Call Stack", "O(b^m)", "O(b * m)", "Yes (finite tree)", "Yes (against optimal opponent)"],
        ["Alpha-Beta Pruning", "Recursive Call Stack", "O(b^(m/2)) [Best Case]", "O(b * m)", "Yes (finite tree)", "Yes (identical to Minimax)"]
    ]
    create_table_grid(doc, headers_cheat, rows_cheat, [1.4, 1.4, 1.3, 1.3, 1.0, 1.07])
