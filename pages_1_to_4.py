from docx_helpers import (
    add_page_header_banner, add_section_heading, add_subheading, 
    add_body_p, add_bullet_point, add_callout_box, create_table_grid, add_ascii_diagram
)
from docx.shared import Pt

def build_page_1(doc):
    # PAGE 1: AI Foundations, Evolution, PEAS & Environments
    add_page_header_banner(doc, 1, "Unit 1: Introduction", "AI Foundations, Evolution, PEAS Framework & Environments")
    
    add_section_heading(doc, "1. What is Artificial Intelligence? Foundations & Human Capabilities")
    add_body_p(doc, 
        "Artificial Intelligence (Russell & Norvig definition) is the study and design of intelligent agents that perceive their environment "
        "and take rational actions to achieve goals. Modern AI focuses on Acting Rationally: an agent is rational if it selects an action "
        "expected to maximize its performance measure given its percept history and built-in knowledge. AI ≠ Omniscience (rationality maximizes EXPECTED success, not actual outcome).",
        "Definition & Paradigm:")
    
    headers_venn = ["Domain", "Core Definition & Philosophy", "Primary Distinction / Hierarchy", "Real-World University Example"]
    rows_venn = [
        ["Artificial Intelligence (AI)", "Broadest discipline: Machines simulating human intelligence, logic, rules, search, learning.", "Grandparent umbrella; includes symbolic rule-based systems and statistical methods.", "Autonomous navigation, Deep Blue chess engine"],
        ["Machine Learning (ML)", "Subset of AI: Systems learning patterns directly from data without being explicitly programmed.", "Data-driven statistical models replacing hard-coded IF-ELSE logical rules.", "Spam filtering, movie recommendation engines"],
        ["Deep Learning (DL)", "Subset of ML: Multi-layered Artificial Neural Networks (ANN) learning hierarchical representations.", "Automatic feature extraction from massive unstructured data (images/audio).", "Face ID unlock, autonomous vehicle vision"],
        ["Natural Language Processing (NLP)", "Intersection of AI, linguistics, and CS: Understanding, parsing, and generating human language.", "Bridges human linguistic communication with machine-executable data structures.", "Chatbots, neural machine translation, voice assistants"]
    ]
    create_table_grid(doc, headers_venn, rows_venn, [1.4, 2.5, 2.0, 1.57])
    
    add_section_heading(doc, "2. Brief History & Evolution of Artificial Intelligence (Milestones)")
    headers_hist = ["Year / Era", "Key Milestone / Breakthrough", "Key Pioneers", "Core Significance to Modern AI"]
    rows_hist = [
        ["1943", "Threshold Logic Unit (First Artificial Neuron Model)", "W. McCulloch & W. Pitts", "Proved simple binary network computes any computable function."],
        ["1950", "Turing Test & 'Computing Machinery and Intelligence'", "Alan Turing", "Operational test for intelligence; proposed machine learning/evolution."],
        ["1956", "Dartmouth Summer Research Project on AI", "J. McCarthy, M. Minsky, C. Shannon", "Official birth of AI as an academic discipline; coined term 'AI'."],
        ["1960s-70s", "Early Optimism, Search & Microworlds (ELIZA, GPS)", "J. Weizenbaum, Newell & Simon", "Demonstrated reasoning; halted by combinatorial explosion."],
        ["1974-80", "First AI Winter (Funding freezes, DARPA cuts)", "Sir James Lighthill (UK Report)", "Failure to scale toy problems to real-world complexity."],
        ["1980-87", "Commercial Expert Systems Boom (XCON, DENDRAL)", "E. Feigenbaum, J. McDermott", "Knowledge-is-power paradigm; saved DEC $40M/year."],
        ["1987-93", "Second AI Winter (Collapse of LISP hardware market)", "Commoditized Desktop PCs", "Specialized hardware collapsed; expert system maintenance proved brittle."],
        ["1993-2011", "Probabilistic Reasoning & Machine Learning Resurgence", "Judea Pearl, IBM (Deep Blue)", "Bayesian networks, SVMs; Deep Blue defeats Kasparov (1997)."],
        ["2012-Pres.", "Deep Learning & Generative AI Revolution", "Hinton, LeCun, Bengio, Vaswani", "AlexNet (2012), AlphaGo (2016), Transformers/LLMs (2017-Present)."]
    ]
    create_table_grid(doc, headers_hist, rows_hist, [0.8, 2.7, 1.8, 2.17])
    
    add_section_heading(doc, "3. Relationship Between Agent & Environment: Rationality & PEAS Framework")
    add_body_p(doc, 
        "An Agent interacts with its Environment in a continuous cycle: Sensors receive percepts from the environment; the Agent Program "
        "processes them; Actuators execute actions affecting the environment. An agent's Rationality depends on: (1) Performance Measure (criterion of success), "
        "(2) Percept Sequence (entire history received to date), (3) Prior Domain Knowledge, and (4) Available Actuators/Actions.",
        "Agent-Environment Loop:")
    
    headers_peas = ["System", "Performance Measure (P)", "Environment (E)", "Actuators (A)", "Sensors (S)"]
    rows_peas = [
        ["Autonomous Taxi Driver", "Safety, speed, legal compliance, passenger comfort, fuel efficiency, profit.", "Public roadways, vehicular traffic, pedestrians, changing weather, roadworks.", "Steering wheel, accelerator, brake pedal, turn signals, horn, display screen.", "LiDAR, radar, RGB cameras, GPS, speedometer, odometer, engine sensors."],
        ["Medical Diagnostic Agent", "Diagnostic accuracy, minimized patient treatment cost, reduced side-effects.", "Hospital patients, clinical staff, laboratory environment, insurance guidelines.", "Screen display of questions, tests ordered, therapy plans, referral notes.", "Keyboard/touchscreen entry of patient symptoms, bloodwork/imaging test feeds."]
    ]
    create_table_grid(doc, headers_peas, rows_peas, [1.4, 1.6, 1.5, 1.5, 1.47])
    
    add_section_heading(doc, "4. Master Classification of Environment Dimensions (7 Dimensions)")
    headers_env = ["Dimension Pair", "Formal Definition & Operational Difference", "Easiest vs Hardest", "Real-World Benchmark Mapping"]
    rows_env = [
        ["Fully vs Partially Observable", "Fully: Agent sensors access complete state at all times. Partially: Noisy/missing sensor data.", "Fully (easy) vs Partially (hard)", "Fully: Chess, 8-Puzzle. Partially: Poker, Taxi Driving."],
        ["Deterministic vs Stochastic", "Deterministic: Next state completely determined by current state and action. Stochastic: Randomness.", "Deterministic vs Stochastic", "Deterministic: Tic-Tac-Toe. Stochastic: Backgammon, Stock Market."],
        ["Episodic vs Sequential", "Episodic: Current decision has no impact on future episodes. Sequential: Current action affects future.", "Episodic vs Sequential", "Episodic: Defect Part Scanning. Sequential: Chess, Driving."],
        ["Static vs Dynamic", "Static: Environment does not change while agent is deliberating. Dynamic: World changes continuously.", "Static vs Dynamic", "Static: Crossword puzzle. Dynamic: Autonomous Taxi Driving."],
        ["Discrete vs Continuous", "Discrete: Finite, distinct states, time steps, and actions. Continuous: Infinite real-valued ranges.", "Discrete vs Continuous", "Discrete: Chess, Checkers. Continuous: Drone Flight, Robot Arm."],
        ["Single vs Multi-Agent", "Single: Agent operates alone. Multi-Agent: Multiple agents interacting (cooperative/competitive).", "Single-Agent vs Multi-Agent", "Single: Solitaire, Sudoku. Multi: Soccer, Chess (Adversarial)."],
        ["Known vs Unknown", "Known: Environment physics/rules known to agent. Unknown: Agent must learn how world works.", "Known vs Unknown", "Known: Solitaire rules known. Unknown: Exploring new video game."]
    ]
    create_table_grid(doc, headers_env, rows_env, [1.3, 2.7, 1.5, 1.97])
    
    add_callout_box(doc, 
        "DBATU EXAM SHORTCUT: In Q1 MCQs, the easiest environment is 'Fully Observable, Deterministic, Static, Discrete, Single-Agent'. "
        "The hardest is 'Partially Observable, Stochastic, Sequential, Dynamic, Continuous, Multi-Agent' (e.g., Autonomous Driving).",
        "High-Yield Exam Takeaway")

def build_page_2(doc):
    # PAGE 2: Structure of Intelligent Agents
    add_page_header_banner(doc, 2, "Unit 1: Intelligent Agents", "Structure of Intelligent Agents — The 5 Agent Architectures")
    
    add_section_heading(doc, "1. Structure of Intelligent Agents: Architecture + Program")
    add_body_p(doc, 
        "Every intelligent agent consists of two fundamental layers: Agent = Architecture + Program. "
        "The Architecture is the physical hardware device (computing unit, camera sensors, motor actuators). "
        "The Agent Program is the concrete software implementation of the mathematical agent function f: P* -> A, which maps any percept history sequence P* to an appropriate action A. "
        "There are 5 standard agent architectures with progressively increasing reasoning power and state representation.",
        "Core Architectural Formula:")
    
    add_section_heading(doc, "2. Detailed Analysis of the 5 Agent Architectures")
    
    # Agent 1
    add_subheading(doc, "Architecture 1: Simple Reflex Agent (Condition-Action Rule Base)")
    add_bullet_point(doc, "Selects actions based exclusively on the current percept, completely ignoring percept history.", "Core Logic:")
    add_bullet_point(doc, "Condition-Action Rules (IF condition THEN action). E.g., IF car_in_front_brakes THEN initiate_braking.", "Knowledge Base:")
    add_bullet_point(doc, "Suffers from infinite loops in partially observable environments; lacks memory and forward foresight.", "Key Limitation:")
    add_ascii_diagram(doc, 
        "[Environment] ---> [Sensors] ---> [Current Percept] ---> [What world is like now]\n"
        "                                                                |\n"
        "[Environment] <--- [Actuators] <--- [Action Selected] <--- [Condition-Action Rules]")
    
    # Agent 2
    add_subheading(doc, "Architecture 2: Model-Based Reflex Agent (Internal State Tracking)")
    add_bullet_point(doc, "Maintains an Internal State to overcome partial observability and handle unobserved aspects of current world.", "Core Logic:")
    add_bullet_point(doc, "(a) Transition Model (How the world evolves independently), (b) Sensor Model (How agent's actions affect the world).", "Two Knowledge Models:")
    add_bullet_point(doc, "Autonomous vehicle overtaking: remembers vehicle hidden in blind spot even when camera cannot see it.", "Concrete Example:")
    add_ascii_diagram(doc, 
        "[Sensors] ---> [State] <=== [How world evolves] + [What my actions do]\n"
        "                 |\n"
        "                 v\n"
        "       [What world is like now] ---> [Condition-Action Rules] ---> [Actuators]")
    
    # Agent 3
    add_subheading(doc, "Architecture 3: Goal-Based Agent (Search & Planning)")
    add_bullet_point(doc, "Combines current state with explicit Goal Descriptions to decide which actions will achieve the desired outcome.", "Core Logic:")
    add_bullet_point(doc, "Integrates Search algorithms (BFS, A*) and Planning systems. Evaluates 'What will happen if I execute action A?'.", "Decision Engine:")
    add_bullet_point(doc, "Highly flexible; if goal changes from Location A to Location B, agent dynamically replans without rule rewrite.", "Advantage:")
    
    # Agent 4
    add_subheading(doc, "Architecture 4: Utility-Based Agent (Trade-Offs & Multi-Objective Optimization)")
    add_bullet_point(doc, "When multiple paths reach a goal, uses a real-valued Utility Function U(s) -> R to measure degree of 'happiness' / quality.", "Core Logic:")
    add_bullet_point(doc, "Balances conflicting objectives under uncertainty (e.g., flight booking balancing speed vs ticket price vs safety).", "Trade-Off Resolution:")
    add_bullet_point(doc, "Selects action maximizing Expected Utility: EU(a) = SUM [ P(Result(s,a) = s') * U(s') ].", "Mathematical Decision Rule:")
    
    # Agent 5
    add_subheading(doc, "Architecture 5: Learning Agent (Self-Improving Lifecycle)")
    add_bullet_point(doc, "Decouples learning from acting so the agent can operate in unknown environments and improve over time.", "Core Logic:")
    add_bullet_point(doc, "Critic (evaluates behavior against external standard) | Learning Element (improves rules/weights) | Problem Generator (suggests exploratory actions) | Performance Element (selects external actions).", "4 Modular Components:")
    add_ascii_diagram(doc, 
        "[Percepts] ---> [Sensors] ---> [Critic] <--- [External Performance Standard]\n"
        "                                  | (Feedback)\n"
        "                                  v\n"
        "                       [Learning Element] ---> [Learning Goals] ---> [Problem Generator]\n"
        "                                  | (Improvements)                      |\n"
        "                                  v                                     v\n"
        "[Actions]  <--- [Actuators] <--- [Performance Element] <----------------+")
    
    add_section_heading(doc, "3. Comprehensive Master Comparison of the 5 Agent Architectures")
    headers_comp = ["Agent Architecture", "Internal State?", "Knowledge Models Used", "Environmental Suitability", "Decision Basis", "Real-World Benchmark"]
    rows_comp = [
        ["Simple Reflex", "No (Memoryless)", "Condition-Action Rules", "Fully Observable Only", "Direct percept mapping", "Thermostat, Automated Vacuum"],
        ["Model-Based Reflex", "Yes (History)", "Transition & Sensor Models", "Partially Observable", "Current state + Rules", "Blind-spot Car Overtaking"],
        ["Goal-Based", "Yes (State)", "Goals + State Transitions", "Complex Sequential", "Search & Planning to Goal", "GPS Navigation, Maze Robot"],
        ["Utility-Based", "Yes (State)", "Utility Function U(s)", "Uncertain & Conflicting", "Expected Utility Maximization", "Automated Financial Trading"],
        ["Learning Agent", "Yes (State & Weights)", "Critic, Learning & Problem Gen.", "Initially Unknown Dynamic", "Experience-driven refinement", "AlphaGo, Self-driving Tesla"]
    ]
    create_table_grid(doc, headers_comp, rows_comp, [1.3, 0.9, 1.4, 1.3, 1.3, 1.27])
    
    add_callout_box(doc, 
        "DBATU LONG ANSWER FORMAT: In Q2.A (Winter 2025) and Q1.C (Summer 2024), draw the block diagrams shown above, "
        "define the 4 sub-modules of the Learning Agent (Critic, Learning Element, Problem Generator, Performance Element), and finish with the comparison table.",
        "Sure-Shot 6-Mark Exam Checklist")

def build_page_3(doc):
    # PAGE 3: Problem Solving & Search: UCS, Heuristics & Hill Climbing
    add_page_header_banner(doc, 3, "Unit 2: Problem-Solving & Search", "Uniform Cost Search (UCS), Heuristics & Hill Climbing")
    
    add_section_heading(doc, "1. Problem-Solving Formulation in State Space")
    add_body_p(doc, 
        "A formal problem is defined by a 5-tuple: (1) Initial State s0, (2) Actions Actions(s), (3) Transition Model Result(s, a), "
        "(4) Goal Test GoalTest(s), and (5) Path Cost c(s, a, s'). The step cost is c(s, a, s') >= eps > 0; total path cost g(n) is the sum of step costs from s0 to n.",
        "Formal Definition:")
    
    add_section_heading(doc, "2. Uniform Cost Search (UCS) Algorithm (Direct PYQ Answer)")
    add_body_p(doc, 
        "Uniform Cost Search is an uninformed search algorithm that expands the unexpanded node n with the lowest cumulative path cost g(n). "
        "It uses a Priority Queue ordered by g(n). It is equivalent to Dijkstra's algorithm generalized to search trees/graphs.",
        "Core Philosophy:")
    
    add_bullet_point(doc, "Initialize frontier as a priority queue ordered by g(n) containing Node(s0, cost=0); explored = empty set.", "Step 1 (Initialization):")
    add_bullet_point(doc, "If frontier is empty, return FAILURE.", "Step 2 (Termination Check):")
    add_bullet_point(doc, "Pop node n with lowest g(n) from frontier.", "Step 3 (Node Selection):")
    add_bullet_point(doc, "CRITICAL: If GoalTest(n.state) == TRUE, return SOLUTION(n). (Goal test applied on expansion, NEVER on generation!)", "Step 4 (Goal Test):")
    add_bullet_point(doc, "Insert n.state into explored set.", "Step 5 (Exploration):")
    add_bullet_point(doc, "For each action in Actions(n.state): child = Result(n.state, action); g(child) = g(n) + c(n, a, child). "
                          "If child not in explored or frontier: insert into frontier. "
                          "If child is in frontier with HIGHER cost: replace frontier node with child (decrease-key).", "Step 6 (Expansion):")
    
    headers_ucs_prop = ["Metric", "UCS Property", "Mathematical Justification / Operational Reason"]
    rows_ucs_prop = [
        ["Completeness", "Complete (YES)", "Guaranteed if all step costs >= eps > 0 (prevents infinite zero-cost paths)."],
        ["Optimality", "Optimal (YES)", "Always finds lowest-cost path because nodes expanded in non-decreasing order of g(n)."],
        ["Time Complexity", "O(b^(1 + floor(C* / eps)))", "Where C* is cost of optimal solution, b is branching factor, eps is minimum step cost."],
        ["Space Complexity", "O(b^(1 + floor(C* / eps)))", "Stores all explored nodes and frontier in memory (Frontier can become very large)."]
    ]
    create_table_grid(doc, headers_ucs_prop, rows_ucs_prop, [1.4, 1.6, 4.47])
    
    add_subheading(doc, "Worked UCS Numerical Trace Example:")
    add_body_p(doc, "Graph: Start=S, Goal=G. Edges: S->A(1), S->B(5), S->C(2), A->G(9), C->G(4), B->G(1).", "Problem:")
    headers_trace = ["Step", "Node Popped", "g(Node)", "Frontier Contents [Node : g(n)]", "Explored Set", "Action / Status"]
    rows_trace = [
        ["1", "Start (S)", "0", "[A:1, C:2, B:5]", "{S}", "Expanded S; generated children A, C, B"],
        ["2", "A", "1", "[C:2, B:5, G:1+9=10]", "{S, A}", "Expanded A; added G(10) to frontier"],
        ["3", "C", "2", "[B:5, G:2+4=6]", "{S, A, C}", "Expanded C; updated G from cost 10 down to 6!"],
        ["4", "B", "5", "[G:5+1=6]", "{S, A, C, B}", "Expanded B; child G has cost 6 (tied)"],
        ["5", "G", "6", "---", "{S, A, C, B, G}", "Goal Popped! Optimal Path = S -> C -> G (Cost = 6)"]
    ]
    create_table_grid(doc, headers_trace, rows_trace, [0.6, 1.1, 0.8, 2.3, 1.4, 1.27])
    
    add_section_heading(doc, "3. Heuristic Functions: Admissibility, Consistency & Dominance")
    add_body_p(doc, 
        "A Heuristic function h(n) estimates the cheapest path cost from node n to a goal state. It incorporates problem-specific knowledge.",
        "Definition:")
    add_bullet_point(doc, "A heuristic is admissible if h(n) <= h*(n) for all n, where h*(n) is true optimal cost to goal. Never overestimates! Ensures A* tree-search optimality.", "Admissibility:")
    add_bullet_point(doc, "A heuristic is consistent (monotonic) if h(n) <= c(n, a, n') + h(n') for every node n and successor n' (Triangle Inequality). Ensures f(n) never decreases along any path.", "Consistency:")
    add_bullet_point(doc, "If h2(n) >= h1(n) for all n, h2 dominates h1. A* using h2 will expand strictly fewer or equal nodes than h1.", "Dominance:")
    
    add_section_heading(doc, "4. Hill Climbing Search (Simple vs Steepest-Ascent)")
    add_body_p(doc, 
        "Hill Climbing is a greedy local search algorithm that moves continuously in the direction of increasing elevation/heuristic value. "
        "It terminates when no neighbor has a higher value.",
        "Mechanism:")
    
    headers_hc = ["Failure Mode / Anomaly", "Topological Problem Structure", "Algorithmic Consequence", "Standard Engineering Remedy"]
    rows_hc = [
        ["Local Maximum", "A peak that is higher than neighboring states, but lower than global maximum.", "Algorithm halts prematurely thinking it reached global best.", "Random-Restart Hill Climbing: Run multiple trials from random initial states."],
        ["Plateau / Flat Local Max", "A flat area where all adjacent neighbors possess identical heuristic value.", "Algorithm wanders randomly or gets stuck in infinite sideways loops.", "Allow limited sideways moves (e.g., max 100 consecutive sideways moves)."],
        ["Ridge", "A sequence of local peaks where slope is steep in directions diagonal to operators.", "Algorithm oscillates back and forth making negligible progress.", "Use macro-operators (combined steps) or Simulated Annealing (P = exp(dE/T))."]
    ]
    create_table_grid(doc, headers_hc, rows_hc, [1.5, 2.3, 1.7, 1.97])

def build_page_4(doc):
    # PAGE 4: A* Search Algorithm, Observations, Proofs & CSP
    add_page_header_banner(doc, 4, "Unit 2: Informed Search & CSP", "A* Search Algorithm, Heuristic Observations & CSP")
    
    add_section_heading(doc, "1. A* Search Algorithm: Formula, Operation & Pseudocode")
    add_body_p(doc, 
        "A* search evaluates nodes by combining g(n) (path cost from start node to n) and h(n) (estimated cost to nearest goal): "
        "f(n) = g(n) + h(n), where f(n) represents the estimated total cost of cheapest solution path passing through node n.",
        "Evaluation Function:")
    
    add_bullet_point(doc, "Maintain OPEN (priority queue ordered by f(n) containing start node s0) and CLOSED (set of expanded nodes).", "Data Structures:")
    add_bullet_point(doc, "Loop: If OPEN is empty, return FAILURE. Pop node n with minimum f(n) from OPEN.", "Step 1 & 2:")
    add_bullet_point(doc, "If GoalTest(n.state) == TRUE, return Solution Path. Else add n.state to CLOSED.", "Step 3:")
    add_bullet_point(doc, "For each neighbor m of n: compute tentative_g = g(n) + c(n, m). "
                          "If m in CLOSED and tentative_g >= g(m), skip. "
                          "If m not in OPEN or tentative_g < g(m): set parent(m) = n, g(m) = tentative_g, f(m) = g(m) + h(m). "
                          "Insert or update m in OPEN.", "Step 4 (Expansion):")
    
    add_section_heading(doc, "2. Critical Observations & Proofs About A* (Direct PYQ Answer)")
    
    headers_a_obs = ["Observation Area", "Mathematical Condition", "Impact on A* Search Behavior", "Formal Exam Proof Sketch"]
    rows_a_obs = [
        ["Admissibility & Optimality (Tree Search)", "h(n) <= h*(n) (Never overestimates)", "Guarantees finding optimal path first; suboptimal goal never expanded.", "Let G2 be suboptimal goal (g(G2) > C*). Let n be unexpanded node on optimal path. f(n) = g(n)+h(n) <= C* < g(G2) = f(G2). Thus n is expanded before G2."],
        ["Consistency & Optimality (Graph Search)", "h(n) <= c(n, a, n') + h(n') (Monotonicity)", "f(n) values are monotonically non-decreasing along any path. Closed nodes never reopened!", "f(n') = g(n') + h(n') = g(n) + c(n, n') + h(n') >= g(n) + h(n) = f(n). Hence first expansion of any node is guaranteed optimal."],
        ["Heuristic = 0 (Blind UCS)", "h(n) = 0 for all n", "f(n) = g(n). Reduces to Uniform Cost Search.", "Explores circles of equal cost; complete & optimal, but explores huge search space."],
        ["Overestimation (h > h*)", "h(n) > h*(n)", "A* runs significantly faster, prunes aggressively, but LOSES OPTIMALITY.", "May prune optimal path because estimated f(n) artificially exceeds suboptimal goal."],
        ["Time & Space Complexity", "Exponential: O(b^d)", "Memory (Space) is the true bottleneck; stores all nodes in memory.", "Iterative Deepening A* (IDA*) and Simplified Memory Bounded A* (SMA*) solve space bottleneck."]
    ]
    create_table_grid(doc, headers_a_obs, rows_a_obs, [1.4, 1.6, 2.0, 2.47])
    
    add_section_heading(doc, "3. Constraint Satisfaction Problems (CSP): Formalism & Algorithms")
    add_body_p(doc, 
        "A Constraint Satisfaction Problem is formally defined by a triple <X, D, C>: "
        "(1) X = {X1, X2, ..., Xn}: A set of variables. "
        "(2) D = {D1, D2, ..., Dn}: A set of domains, where Di is the set of allowable values for variable Xi. "
        "(3) C = {C1, C2, ..., Cm}: A set of constraints specifying allowable combinations of values.",
        "Formal Triple <X, D, C>:")
    
    add_subheading(doc, "Constraint Propagation & AC-3 Algorithm (Arc Consistency):")
    add_body_p(doc, 
        "A directed arc (Xi, Xj) is arc consistent if for every value x in Di, there exists at least one legal value y in Dj satisfying the constraint. "
        "AC-3 maintains a queue of all arcs. When an arc (Xi, Xj) is examined, if a value in Di has no match in Dj, it is removed from Di. "
        "Whenever Di is modified, all incoming arcs (Xk, Xi) are re-added to the queue. Complexity: O(c * d^3), where c is constraints, d is max domain size.",
        "AC-3 Mechanism:")
    
    headers_csp_h = ["CSP Heuristic", "Operational Heuristic Strategy", "Intuitive Purpose / Why it Works", "Exam Example (Map Coloring)"]
    rows_csp_h = [
        ["MRV (Minimum Remaining Values)", "Choose the variable with the fewest remaining legal values in its domain.", "'Fail-First' Principle: Detects dead ends immediately before wasting deep search.", "Select South Australia (SA) when its domain has shrunk to only 1 color."],
        ["Degree Heuristic", "Tie-breaker for MRV: Choose variable involved in largest number of constraints with unassigned variables.", "Reduces branching factor for future unassigned choices most aggressively.", "SA is picked first because it borders 5 other territories (WA, NT, Q, NSW, V)."],
        ["Least Constraining Value (LCV)", "Given a chosen variable, choose the value that rules out the fewest choices for neighboring variables.", "'Fail-Last' Principle: Leaves maximum future flexibility for remaining variables.", "Choose Green for WA if Green leaves Red and Blue open for NT and SA."]
    ]
    create_table_grid(doc, headers_csp_h, rows_csp_h, [1.5, 2.2, 1.9, 1.87])
    
    add_callout_box(doc, 
        "DBATU EXAM SHORTCUT: For CSP questions, write the triple <X, D, C>, state the AC-3 algorithm queue mechanism, "
        "and explain MRV (Fail-First) vs LCV (Fail-Last). In Map Coloring: Variables = {WA, NT, SA, Q, NSW, V, T}, Domains = {Red, Green, Blue}.",
        "CSP High-Scoring Template")
