from enum import Enum
from typing import (
    Optional,
    Dict,
    List,
    Union,
    Literal,
    Any,
    TypedDict,
)

from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
)
from openai.types.chat.completion_create_params import FunctionCall, ResponseFormat
from openai.types.create_embedding_response import Usage
from pydantic import BaseModel


class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    FUNCTION = "function"
    TOOL = "tool"


class ErrorResponse(BaseModel):
    object: str = "error"
    message: str
    code: int


class ChatCompletionCreateParams(BaseModel):
    messages: List[ChatCompletionMessageParam]
    """A list of messages comprising the conversation so far.

    [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).
    """

    model: str
    """ID of the model to use.

    See the
    [model endpoint compatibility](https://platform.openai.com/docs/models/model-endpoint-compatibility)
    table for details on which models work with the Chat API.
    """

    frequency_penalty: Optional[float] = 0.
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.

    [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/gpt/parameter-details)
    """

    function_call: Optional[FunctionCall] = None
    """Deprecated in favor of `tool_choice`.

    Controls which (if any) function is called by the model. `none` means the model
    will not call a function and instead generates a message. `auto` means the model
    can pick between generating a message or calling a function. Specifying a
    particular function via `{"name": "my_function"}` forces the model to call that
    function.

    `none` is the default when no functions are present. `auto`` is the default if
    functions are present.
    """

    functions: Optional[List] = None
    """Deprecated in favor of `tools`.

    A list of functions the model may generate JSON inputs for.
    """

    logit_bias: Optional[Dict[str, int]] = None
    """Modify the likelihood of specified tokens appearing in the completion.

    Accepts a JSON object that maps tokens (specified by their token ID in the
    tokenizer) to an associated bias value from -100 to 100. Mathematically, the
    bias is added to the logits generated by the model prior to sampling. The exact
    effect will vary per model, but values between -1 and 1 should decrease or
    increase likelihood of selection; values like -100 or 100 should result in a ban
    or exclusive selection of the relevant token.
    """

    logprobs: Optional[bool] = False
    """Whether to return log probabilities of the output tokens or not.

    If true, returns the log probabilities of each output token returned in the
    `content` of `message`. This option is currently not available on the
    `gpt-4-vision-preview` model.
    """

    max_tokens: Optional[int] = None
    """The maximum number of [tokens](/tokenizer) to generate in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
    for counting tokens.
    """

    n: Optional[int] = 1
    """How many chat completion choices to generate for each input message."""

    presence_penalty: Optional[float] = 0.
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.

    [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/gpt/parameter-details)
    """

    response_format: Optional[ResponseFormat] = None
    """An object specifying the format that the model must output.

    Used to enable JSON mode.
    """

    seed: Optional[int] = None
    """This feature is in Beta.

    If specified, our system will make a best effort to sample deterministically,
    such that repeated requests with the same `seed` and parameters should return
    the same result. Determinism is not guaranteed, and you should refer to the
    `system_fingerprint` response parameter to monitor changes in the backend.
    """

    stop: Optional[Union[str, List[str]]] = None
    """Up to 4 sequences where the API will stop generating further tokens."""

    temperature: Optional[float] = 0.9
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.

    We generally recommend altering this or `top_p` but not both.
    """

    tool_choice: Optional[ChatCompletionToolChoiceOptionParam] = None
    """
    Controls which (if any) function is called by the model. `none` means the model
    will not call a function and instead generates a message. `auto` means the model
    can pick between generating a message or calling a function. Specifying a
    particular function via
    `{"type: "function", "function": {"name": "my_function"}}` forces the model to
    call that function.

    `none` is the default when no functions are present. `auto` is the default if
    functions are present.
    """

    tools: Optional[List] = None
    """A list of tools the model may call.

    Currently, only functions are supported as a tool. Use this to provide a list of
    functions the model may generate JSON inputs for.
    """

    top_logprobs: Optional[int] = None
    """
    An integer between 0 and 5 specifying the number of most likely tokens to return
    at each token position, each with an associated log probability. `logprobs` must
    be set to `true` if this parameter is used.
    """

    top_p: Optional[float] = 1.0
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    user: Optional[str] = None
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse.
    [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
    """

    stream: Optional[bool] = False
    """If set, partial message deltas will be sent, like in ChatGPT.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).
    """

    # Addictional parameters
    repetition_penalty: Optional[float] = 1.03
    """The parameter for repetition penalty. 1.0 means no penalty.
    See[this paper](https://arxiv.org / pdf / 1909.05858.pdf) for more details.
    """

    typical_p: Optional[float] = None
    """Typical Decoding mass.
    See[Typical Decoding for Natural Language Generation](https://arxiv.org / abs / 2202.00666) for more information
    """

    watermark: Optional[bool] = False
    """Watermarking with [A Watermark for Large Language Models](https://arxiv.org / abs / 2301.10226)
    """

    best_of: Optional[int] = 1

    ignore_eos: Optional[bool] = False

    use_beam_search: Optional[bool] = False

    stop_token_ids: Optional[List[int]] = None

    skip_special_tokens: Optional[bool] = True

    spaces_between_special_tokens: Optional[bool] = True

    min_p: Optional[float] = 0.0

    include_stop_str_in_output: Optional[bool] = False

    length_penalty: Optional[float] = 1.0

    guided_json: Optional[Union[str, dict, BaseModel]] = None

    guided_regex: Optional[str] = None

    guided_choice: Optional[List[str]] = None

    guided_grammar: Optional[str] = None


class CompletionCreateParams(BaseModel):
    model: str
    """ID of the model to use.

    You can use the
    [List models](https://platform.openai.com/docs/api-reference/models/list) API to
    see all of your available models, or see our
    [Model overview](https://platform.openai.com/docs/models/overview) for
    descriptions of them.
    """

    prompt: Union[str, List[str], List[int], List[List[int]], None]
    """
    The prompt(s) to generate completions for, encoded as a string, array of
    strings, array of tokens, or array of token arrays.

    Note that <|endoftext|> is the document separator that the model sees during
    training, so if a prompt is not specified the model will generate as if from the
    beginning of a new document.
    """

    best_of: Optional[int] = 1
    """
    Generates `best_of` completions server-side and returns the "best" (the one with
    the highest log probability per token). Results cannot be streamed.

    When used with `n`, `best_of` controls the number of candidate completions and
    `n` specifies how many to return – `best_of` must be greater than `n`.

    **Note:** Because this parameter generates many completions, it can quickly
    consume your token quota. Use carefully and ensure that you have reasonable
    settings for `max_tokens` and `stop`.
    """

    echo: Optional[bool] = False
    """Echo back the prompt in addition to the completion"""

    frequency_penalty: Optional[float] = 0.
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on their existing frequency in the
    text so far, decreasing the model's likelihood to repeat the same line verbatim.

    [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/gpt/parameter-details)
    """

    logit_bias: Optional[Dict[str, int]] = None
    """Modify the likelihood of specified tokens appearing in the completion.

    Accepts a JSON object that maps tokens (specified by their token ID in the GPT
    tokenizer) to an associated bias value from -100 to 100. You can use this
    [tokenizer tool](/tokenizer?view=bpe) (which works for both GPT-2 and GPT-3) to
    convert text to token IDs. Mathematically, the bias is added to the logits
    generated by the model prior to sampling. The exact effect will vary per model,
    but values between -1 and 1 should decrease or increase likelihood of selection;
    values like -100 or 100 should result in a ban or exclusive selection of the
    relevant token.

    As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
    from being generated.
    """

    logprobs: Optional[int] = None
    """
    Include the log probabilities on the `logprobs` most likely tokens, as well the
    chosen tokens. For example, if `logprobs` is 5, the API will return a list of
    the 5 most likely tokens. The API will always return the `logprob` of the
    sampled token, so there may be up to `logprobs+1` elements in the response.

    The maximum value for `logprobs` is 5.
    """

    max_tokens: Optional[int] = 16
    """The maximum number of [tokens](/tokenizer) to generate in the completion.

    The token count of your prompt plus `max_tokens` cannot exceed the model's
    context length.
    [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
    for counting tokens.
    """

    n: Optional[int] = 1
    """How many completions to generate for each prompt.

    **Note:** Because this parameter generates many completions, it can quickly
    consume your token quota. Use carefully and ensure that you have reasonable
    settings for `max_tokens` and `stop`.
    """

    presence_penalty: Optional[float] = 0.
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.

    [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/gpt/parameter-details)
    """

    seed: Optional[int] = None
    """
    If specified, our system will make a best effort to sample deterministically,
    such that repeated requests with the same `seed` and parameters should return
    the same result.

    Determinism is not guaranteed, and you should refer to the `system_fingerprint`
    response parameter to monitor changes in the backend.
    """

    stop: Optional[Union[str, List[str]]] = None
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    suffix: Optional[str] = None
    """The suffix that comes after a completion of inserted text."""

    temperature: Optional[float] = 1.
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.

    We generally recommend altering this or `top_p` but not both.
    """

    top_p: Optional[float] = 1.
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or `temperature` but not both.
    """

    user: Optional[str] = None
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse.
    [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
    """

    stream: Optional[bool] = False
    """If set, partial message deltas will be sent, like in ChatGPT.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).
    """

    # Addictional parameters
    repetition_penalty: Optional[float] = 1.03
    """The parameter for repetition penalty. 1.0 means no penalty.
    See[this paper](https://arxiv.org / pdf / 1909.05858.pdf) for more details.
    """

    typical_p: Optional[float] = None
    """Typical Decoding mass.
    See[Typical Decoding for Natural Language Generation](https://arxiv.org / abs / 2202.00666) for more information
    """

    watermark: Optional[bool] = False
    """Watermarking with [A Watermark for Large Language Models](https://arxiv.org / abs / 2301.10226)
    """

    ignore_eos: Optional[bool] = False

    use_beam_search: Optional[bool] = False

    stop_token_ids: Optional[List[int]] = None

    skip_special_tokens: Optional[bool] = True

    spaces_between_special_tokens: Optional[bool] = True

    min_p: Optional[float] = 0.0

    include_stop_str_in_output: Optional[bool] = False

    length_penalty: Optional[float] = 1.0

    guided_json: Optional[Union[str, dict, BaseModel]] = None

    guided_regex: Optional[str] = None

    guided_choice: Optional[List[str]] = None

    guided_grammar: Optional[str] = None


class EmbeddingCreateParams(BaseModel):
    input: Union[str, List[str], List[int], List[List[int]]]
    """Input text to embed, encoded as a string or array of tokens.

    To embed multiple inputs in a single request, pass an array of strings or array
    of token arrays. The input must not exceed the max input tokens for the model
    (8192 tokens for `text-embedding-ada-002`) and cannot be an empty string.
    [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
    for counting tokens.
    """

    model: str
    """ID of the model to use.

    You can use the
    [List models](https://platform.openai.com/docs/api-reference/models/list) API to
    see all of your available models, or see our
    [Model overview](https://platform.openai.com/docs/models/overview) for
    descriptions of them.
    """

    encoding_format: Literal["float", "base64"] = "float"
    """The format to return the embeddings in.

    Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).
    """

    dimensions: Optional[int] = None
    """The number of dimensions the resulting output embeddings should have.

    Only supported in `text-embedding-3` and later models.
    """

    user: Optional[str] = None
    """
    A unique identifier representing your end-user, which can help OpenAI to monitor
    and detect abuse.
    [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).
    """


class Embedding(BaseModel):
    embedding: Any
    """The embedding vector, which is a list of floats.

    The length of vector depends on the model as listed in the
    [embedding guide](https://platform.openai.com/docs/guides/embeddings).
    """

    index: int
    """The index of the embedding in the list of embeddings."""

    object: Literal["embedding"]
    """The object type, which is always "embedding"."""


class CreateEmbeddingResponse(BaseModel):
    data: List[Embedding]
    """The list of embeddings generated by the model."""

    model: str
    """The name of the model used to generate the embedding."""

    object: Literal["list"]
    """The object type, which is always "list"."""

    usage: Usage
    """The usage information for the request."""


class RerankRequest(BaseModel):
    model: str
    """The name of the model used to rerank."""

    query: str
    """The query for rerank."""

    documents: List[str]
    """The documents for rerank."""

    top_n: Optional[int] = None

    return_documents: Optional[bool] = False


class Document(TypedDict):
    text: str


class DocumentObj(TypedDict):
    index: int
    relevance_score: float
    document: Optional[Document]


class RerankResponse(TypedDict):
    id: Optional[str]
    results: List[DocumentObj]
