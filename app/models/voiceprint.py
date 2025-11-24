from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class VoiceprintRegisterRequest(BaseModel):
    """声纹注册请求模型"""

    speaker_id: str

    model_config = ConfigDict(json_schema_extra={"example": {"speaker_id": "user_001"}})


class VoiceprintRegisterResponse(BaseModel):
    """声纹注册响应模型"""

    success: bool
    msg: str

    model_config = ConfigDict(json_schema_extra={"example": {"success": True, "msg": "已登记: user_001"}})


class VoiceprintIdentifyRequest(BaseModel):
    """声纹识别请求模型"""

    speaker_ids: str  # 逗号分隔的候选说话人ID

    model_config = ConfigDict(json_schema_extra={"example": {"speaker_ids": "user_001,user_002,user_003"}})


class VoiceprintIdentifyResponse(BaseModel):
    """声纹识别响应模型"""

    speaker_id: str
    score: float

    model_config = ConfigDict(json_schema_extra={"example": {"speaker_id": "user_001", "score": 0.85}})
