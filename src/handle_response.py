def handle_response(inputs):
    custom_output_params = {
        "output_param": inputs["input_results"]
    }
    return workflow.log.done("Action completed successfully", {}, custom_output_params)