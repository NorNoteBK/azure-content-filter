import azure.functions as func
import logging
import json

app = func.FunctionApp()

@app.route(route="filter_comment", auth_level=func.AuthLevel.ANONYMOUS)
def filter_comment(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON body",
            status_code=400
        )

    comment = req_body.get('comment')
    if not comment:
        return func.HttpResponse(
            "Please pass a comment in the request body",
            status_code=400
        )

    # Filtering logic
    bad_words = ["bad", "terrible", "worst"]
    filtered_comment = comment
    is_safe = True

    for word in bad_words:
        if word.lower() in filtered_comment.lower():
            is_safe = False
            # Simple case-insensitive replacement (imperfect but functional for this demo)
            # A more robust regex solution could be used for better matching
            import re
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            filtered_comment = pattern.sub("****", filtered_comment)

    response_body = {
        "original": comment,
        "filtered": filtered_comment,
        "is_safe": is_safe
    }

    return func.HttpResponse(
        json.dumps(response_body),
        mimetype="application/json",
        status_code=200
    )
