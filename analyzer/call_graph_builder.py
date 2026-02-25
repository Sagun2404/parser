from core.relationship import Relationship

def build_call_graph(entities, relationships):
    # 1. Create a lookup map of all definitions (functions/classes)
    # We map name -> entity_id for quick searching
    definitions = {
        e.name: e.id 
        for e in entities 
        if e.type in ["function", "class"]
    }

    # 2. Iterate through all entities to find 'calls'
    for entity in entities:
        if entity.type == "call":
            # Check if the name of the call matches a known definition
            # (Note: You might need to strip parens/arguments if your name is "square(10)")
            call_name = entity.name.split('(')[0].split('.')[-1]
            
            if call_name in definitions:
                target_id = definitions[call_name]
                
                # 3. Create a 'calls' relationship
                # The source is the PARENT of the call (e.g., the function it's inside)
                # or the call entity itself. Usually, we link caller_func -> callee_func.
                relationships.append(
                    Relationship(
                        source_id=entity.parent_id or entity.id, 
                        target_id=target_id,
                        type="calls"
                    )
                )
    
    return relationships