from mistralai import Mistral

from app.config import AI_TOKEN


async def gen(content):
    s = Mistral(api_key=AI_TOKEN)
    res = await s.chat.complete_async(model="mistral-large-latest", messages=[
        {
            "content": f"Напиши подробный рецепт блюда по описанию которое я написал ниже."
                       f"Рецепт должен содержать в себе ингредиенты, их количество и способ приготовления."
                       f"Описание блюда: {content}",
            "role": "user",
        },
    ])
    if res is not None:
        return res.choices[0].message.content
