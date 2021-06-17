# Define all headers that affect the YAML File

classCode = "Question code / Key"
question = "Question"
group = "Disp. Group"
order = "Order"


# Write headers that are useless to the yaml output
to_be_dropped = ["Wave", "Notes / Questions / Decision", "Card", "Screen"]

# Change Dict Key based on the grouping column
grouping_enum = {
    "ClassRelated": "classSpecific",
    "General": "generic",
    "ClaimHistory": "priorClaims",
}
