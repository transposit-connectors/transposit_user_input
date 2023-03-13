def handle_response(inputs):
    custom_output_params = {
        "outputs": inputs["input_results"]
    }
    return workflow.log.done("", {}, custom_output_params)