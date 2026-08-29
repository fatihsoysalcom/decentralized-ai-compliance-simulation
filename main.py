import random

# --- Simulated Decentralized AI Collective Nodes ---
# Each node represents an AI entity with specific attributes, potentially across different jurisdictions.
AI_NODES = [
    {"id": "node_alpha", "origin_country": "USA", "capabilities": ["data_analysis", "prediction"]},
    {"id": "node_beta", "origin_country": "EU", "capabilities": ["image_recognition", "nlp"]},
    {"id": "node_gamma", "origin_country": "China", "capabilities": ["data_analysis", "optimization"]},
    {"id": "node_delta", "origin_country": "Russia", "capabilities": ["nlp", "cyber_security"]},
    {"id": "node_epsilon", "origin_country": "USA", "capabilities": ["prediction", "optimization"]},
    {"id": "node_zeta", "origin_country": "Iran", "capabilities": ["data_analysis", "image_recognition"]},
]

# --- Simulated Tasks for the Collective ---
# Each task requires a specific capability and targets a region, representing a potential use case.
TASKS = [
    {"id": "task_001", "description": "Analyze global market trends", "required_capability": "data_analysis", "target_country": "Global"},
    {"id": "task_002", "description": "Develop new language model for EU", "required_capability": "nlp", "target_country": "EU"},
    {"id": "task_003", "description": "Predict regional resource scarcity", "required_capability": "prediction", "target_country": "Africa"},
    {"id": "task_004", "description": "Optimize supply chain logistics", "required_capability": "optimization", "target_country": "USA"},
    {"id": "task_005", "description": "Identify satellite imagery anomalies", "required_capability": "image_recognition", "target_country": "Middle_East"},
    {"id": "task_006", "description": "Cyber threat assessment for critical infrastructure", "required_capability": "cyber_security", "target_country": "USA"},
    {"id": "task_007", "description": "Market sentiment analysis in China", "required_capability": "data_analysis", "target_country": "China"},
    {"id": "task_008", "description": "Predict election outcomes", "required_capability": "prediction", "target_country": "USA"},
]

# --- Simulated Sanctions and Compliance Rules ---
# This represents the "geopolitical intersection" and "compliance challenge" discussed in the article.
# Rules can restrict nodes from certain origins operating in certain targets, or restrict specific capabilities.
SANCTIONS_RULES = [
    # Example 1: Node from 'China' cannot perform 'cyber_security' tasks anywhere.
    {"type": "capability_restriction", "origin": "China", "restricted_capability": "cyber_security", "reason": "National Security Concerns"},
    # Example 2: Node from 'Russia' cannot operate in 'USA' for any task.
    {"type": "geopolitical_ban", "origin": "Russia", "target": "USA", "reason": "Bilateral Sanctions"},
    # Example 3: Node from 'Iran' cannot perform 'prediction' tasks anywhere.
    {"type": "capability_restriction", "origin": "Iran", "restricted_capability": "prediction", "reason": "Proliferation Risk"},
    # Example 4: Node from 'USA' cannot operate in 'China' for 'data_analysis' tasks.
    {"type": "geopolitical_capability_ban", "origin": "USA", "target": "China", "restricted_capability": "data_analysis", "reason": "Data Sovereignty"},
]

def check_compliance(node, task, sanctions_rules):
    """
    Checks if a given AI node is compliant to perform a specific task
    based on the defined sanctions rules. This models the 'control mechanisms'
    and 'transparency' challenges for decentralized AI.
    """
    node_origin = node["origin_country"]
    task_target = task["target_country"]
    task_capability = task["required_capability"]

    for rule in sanctions_rules:
        if rule["type"] == "capability_restriction":
            # Rule: A specific capability is restricted for nodes from a certain origin.
            if rule["origin"] == node_origin and rule["restricted_capability"] == task_capability:
                return False, f"Capability '{task_capability}' restricted for '{node_origin}' (Reason: {rule['reason']})"
        
        elif rule["type"] == "geopolitical_ban":
            # Rule: Nodes from a certain origin are banned from operating in a specific target region.
            if rule["origin"] == node_origin and (rule["target"] == task_target or rule["target"] == "Global"):
                return False, f"Node from '{node_origin}' banned from operating in '{task_target}' (Reason: {rule['reason']})"
        
        elif rule["type"] == "geopolitical_capability_ban":
            # Rule: A specific capability from a certain origin is banned in a specific target region.
            if rule["origin"] == node_origin and (rule["target"] == task_target or rule["target"] == "Global") and rule["restricted_capability"] == task_capability:
                return False, f"Node from '{node_origin}' cannot perform '{task_capability}' in '{task_target}' (Reason: {rule['reason']})"
    
    # If no rule is violated, the node is compliant for this task.
    return True, "Compliant"

def main():
    print("--- Simulating A/I Collective Task Assignment with Sanctions ---\n")

    for task in TASKS:
        print(f"Attempting to assign Task: '{task['description']}' (ID: {task['id']})")
        print(f"  Required Capability: '{task['required_capability']}', Target: '{task['target_country']}'")
        
        eligible_nodes = []
        for node in AI_NODES:
            # First, check if the node has the required capability for the task.
            if task["required_capability"] in node["capabilities"]:
                # Second, check for compliance with geopolitical sanctions.
                is_compliant, reason = check_compliance(node, task, SANCTIONS_RULES)
                if is_compliant:
                    eligible_nodes.append(node)
                else:
                    print(f"    Node '{node['id']}' from '{node['origin_country']}' is NOT compliant for this task. {reason}")
            else:
                print(f"    Node '{node['id']}' from '{node['origin_country']}' lacks required capability '{task['required_capability']}'.")

        if eligible_nodes:
            # In a real decentralized system, this might involve complex negotiation or consensus.
            # Here, we just pick one randomly for demonstration purposes.
            assigned_node = random.choice(eligible_nodes)
            print(f"  SUCCESS: Task '{task['id']}' assigned to Node '{assigned_node['id']}' from '{assigned_node['origin_country']}'.")
        else:
            # This scenario highlights the 'compliance difficulty' when no node can legally perform the task.
            print(f"  FAILURE: No compliant AI node found to perform Task '{task['id']}'.")
        print("-" * 60)

if __name__ == "__main__":
    main()
