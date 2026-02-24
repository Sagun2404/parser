from core.relationship import Relationship


def build_call_graph(entities, relationships):
    function_map = {}
    calls = []

    # Index functions/methods
    for entity in entities:
        if entity.type in ["function", "method"]:
            function_map[entity.name] = entity

    # Collect call entities
    for entity in entities:
        if entity.type == "call":
            calls.append(entity)

    # Resolve calls
    for call in calls:
        caller = None

        # Find parent function
        for entity in entities:
            if entity.id == call.parent_id and entity.type in ["function", "method"]:
                caller = entity
                break

        callee = function_map.get(call.name)

        if caller and callee:
            relationships.append(
                Relationship(
                    source_id=caller.id,
                    target_id=callee.id,
                    type="calls"
                )
            )

    return relationships