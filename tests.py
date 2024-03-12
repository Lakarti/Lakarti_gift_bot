# ДЛЯ ВИДЕО НО ДОЛГО ГРУЗИТ
# @router.callback_query(F.data == '60*120')
# async def products_60_120(callback: types.CallbackQuery, state: FSMContext):
#     video_url = 'https://video.wbstatic.net/video/new/126750000/126756271.mp4'
#     product_url = 'https://www.wildberries.ru/catalog/126756271/detail.aspx'

#     # Получаем данные из состояния
#     state_data = await state.get_data()
#     files_ids = state_data.get('files_ids', [])

#     # Проверяем, есть ли уже сохраненный файл
#     local_file_path = 'saved_video.mp4'
#     if not os.path.exists(local_file_path):
#         # Если нет, загружаем видео и сохраняем его локально
#         response = requests.get(video_url)
#         with open(local_file_path, 'wb') as video_file:
#             video_file.write(response.content)

#     if files_ids:
#         # Если есть файлы в списке, отправляем первый из них
#         video_file_id = files_ids[0]
#         await callback.message.answer_video(video_file_id, supports_streaming=True)
#     else:
#         # Если список пуст, загружаем новый файл
#         video_file = FSInputFile('saved_video.mp4')
#         result = await callback.message.answer_video(video_file, supports_streaming=True)
#         files_ids.append(result.video.file_id)

#     # Сохраняем обновленные данные в состоянии
#     await state.update_data(files_ids=files_ids)

#     # Отправка ссылки на товар
#     await callback.message.answer(product_url, parse_mode='HTML')