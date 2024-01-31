import os
import re
from plugins import register, Plugin, Event, Reply, ReplyType

@register
class NasSearch(Plugin):
    name = "nas_search"

    def __init__(self, config):
        super().__init__(config)
        self.drives = {f"{drive}:\\": f"{config['base_path']}{folder}" for drive, folder in config['drives'].items()}

    def search_files(self, local_directory, network_directory, keyword):
        files_found = []
        for entry in os.scandir(local_directory):
            if entry.is_dir(follow_symlinks=False):
                try:
                    new_network_directory = os.path.join(network_directory, entry.name)
                    files_found += self.search_files(entry.path, new_network_directory, keyword)
                except PermissionError:
                    pass
            else:
                if keyword.lower() in entry.name.lower():
                    files_found.append(os.path.join(network_directory, entry.name))
        return files_found

    def did_receive_message(self, event: Event):
        query = event.message.content.strip().lower()
        is_group = event.message.is_group

        if is_group:
            query = re.sub(r'@[\w]+\s+', '', query, count=1).strip()

        commands = [cmd.lower() for cmd in self.config.get("command", [])]
        for cmd in commands:
            if query.startswith(cmd):
                keyword = query.split("：", 1)[1]
                files_found = []
                for local_path, network_path in self.drives.items():
                    files_found += self.search_files(local_path, network_path, keyword)

                if not files_found:
                    result_text = "未找到该文件，请检查名称是否正确。"
                else:
                    result_text = "找到以下文件：\n" + "\n".join(files_found)

                reply = Reply(ReplyType.TEXT, result_text.strip())
                event.channel.send(reply, event.message)
                event.bypass()
                break

    def help(self, **kwargs) -> str:
        return "发送 '搜索NAS：[文件名]' 或 '查找NAS：[文件名]' 来搜索文件。"

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def will_generate_reply(self, event: Event):
        pass
