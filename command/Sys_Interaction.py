# Assistant (TO DO: Implement this: Computer File Interaction Requests)
# run = client.beta.threads.create_and_run(
#     assistant_id=assistant.id,
#     instructions=f"Please address the user as {USER_NAME}."
# )
# # Add question to thread
# inRun = True
# while (inRun):
#     if run.status == 'completed': 
#         messages = client.beta.threads.messages.list(
#             thread_id=thread.id
#         )
#         print(f'Myra: {messages[-1].content}')
#         inRun = False
#     else:
#         print(run.status)