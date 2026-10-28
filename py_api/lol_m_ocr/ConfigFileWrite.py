
class ConfigFileWrite():
    def __init__(self, conf_data, conf_type, save_file):
        self.conf_data = conf_data
        self.conf_type = conf_type
        self.save_file = save_file

    def write_conf(self):
        if self.conf_type == 'toml' or self.conf_type == 'TOML':
            self.save_file = self.write_config_toml(self.conf_data, self.save_file)
        elif self.conf_type == 'hocon' or self.conf_type == 'HOCON':
            self.save_file = self.write_config_hocon(self.conf_data, self.save_file)
        elif self.conf_type == 'json' or self.conf_type == 'JSON':
            self.save_file = self.write_config_json(self.conf_data, self.save_file)
        elif self.conf_type == 'yaml' or self.conf_type == 'YAML':
            self.save_file = self.write_config_yaml(self.conf_data, self.save_file)
        elif self.conf_type == 'ini' or self.conf_type == 'INI':
            self.save_file = self.write_config_ini(self.conf_data, self.save_file)
        elif self.conf_type == 'properties' or self.conf_type == 'PROPERTIES':
            self.save_file = self.write_config_properties(self.conf_data, self.save_file)
        else:
            logger.error('读取文件类型不支持。支持的文件类型{}'.format(self.file_type))
            return False

        return self.save_file

    @staticmethod
    def write_config_toml(conf_data, save_file):
        """
        写入toml文件
        :param conf_data: dict结构的数据
        :param save_file: 文件保存路径
        :return: 成功返回保存路径，失败返回False
        """
        try:
            if save_file is None:
                logger.error('存放路径不存在')
                return False
            if conf_data is None:
                logger.error('配置{}为空或不存在'.format(conf_data))
                return False
            with open(save_file, 'w', encoding='utf-8') as f:
                toml.dump(o=dict(conf_data), f=f)
        except Exception as e:
            logger.error('配置保存失败，{}'.format(str(e)))
            return False
        return save_file

    @staticmethod
    def write_config_hocon(conf_data, save_file):
        """
        写入hocon文件
        :param conf_data: dict结构的数据
        :param save_file: 文件保存路径
        :return: 成功返回保存路径，失败返回False
        """
        try:
            if save_file is None:
                logger.error('存放路径不存在')
                return False
            if conf_data is None:
                logger.error('配置{}为空或不存在'.format(conf_data))
                return False
            config_tree = ConfigFactory.from_dict(dict(conf_data))
            res = HOCONConverter.convert(config_tree, 'hocon')
            with open(save_file, "w") as fd:
                fd.write(res)
        except Exception as e:
            logger.error('配置保存失败，{}'.format(str(e)))
            return False

    @staticmethod
    def write_config_json(conf_data, save_file):
        """
        写入json文件
        :param conf_data: dict结构的数据
        :param save_file: 文件保存路径
        :return: 成功返回保存路径，失败返回False
        """
        try:
            if save_file is None:
                logger.error('存放路径不存在')
                return False
            if conf_data is None:
                logger.error('配置{}为空或不存在'.format(conf_data))
                return False
            save_str = json.dumps(conf_data)
            with open(save_file, 'w') as fp:
                fp.write(save_str)
        except Exception as e:
            logger.error('配置保存失败，{}'.format(str(e)))
            return False
        return save_file

    @staticmethod
    def write_config_yaml(conf_data, save_file):
        """
        写入yaml文件
        :param conf_data: dict结构的数据
        :param save_file: 文件保存路径
        :return: 成功返回保存路径，失败返回False
        """
        try:
            if save_file is None:
                logger.error('存放路径不存在')
                return False
            if conf_data is None:
                logger.error('配置{}为空或不存在'.format(conf_data))
                return False
            with open(save_file, 'w', encoding='utf-8') as f:
                yaml.dump(data=dict(conf_data), stream=f, allow_unicode=True)
        except Exception as e:
            logger.error('配置保存失败，{}'.format(str(e)))
            return False
        return save_file

    @staticmethod
    def write_config_ini(conf_data, save_file):
        """
        写入json文件
        :param conf_data: dict结构的数据
        :param save_file: 文件保存路径
        :return: 成功返回保存路径，失败返回False
        """
        try:
            if save_file is None:
                logger.error('存放路径不存在')
                return False
            if conf_data is None:
                logger.error('配置{}为空或不存在'.format(conf_data))
                return False
            config = ConfigParser()
            config.read_dict(dict(conf_data))
            with open(save_file, 'w', encoding='utf-8') as f:
                config.write(f)
        except Exception as e:
            logger.error('配置保存失败，{}'.format(str(e)))
            return False
        return save_file

    @staticmethod
    def write_config_properties(conf_data, save_file):
        """
        写入property文件
        :param conf_data: dict结构的数据
        :param save_file: 文件保存路径
        :return: 成功返回保存路径，失败返回False
        """
        try:
            if save_file is None:
                logger.error('存放路径不存在')
                return False
            if conf_data is None:
                logger.error('配置{}为空或不存在'.format(conf_data))
                return False
            config_tree = ConfigFactory.from_dict(dict(conf_data))
            res = HOCONConverter.convert(config_tree, 'properties')
            with open(save_file, "w") as fd:
                fd.write(res)
        except Exception as e:
            logger.error('配置保存失败，{}'.format(str(e)))
            return False
        return save_file

if __name__ == '__main__':

    save_ini = r'D:\work\bussiness\dd.ini'
    save_file = r'D:\work\dd.yaml'

    conf = ConfigFileRead.read_config_ini(save_ini)
 
    # save_path = ConfigFileWrite(conf_data=conf, conf_type='ini', save_file=save_file).write_conf()
    # save_path = ConfigFileWrite(conf_data=conf, conf_type='yaml', save_file=save_file).write_conf()
    # save_path = ConfigFileWrite(conf_data=conf, conf_type='toml', save_file=save_file).write_conf()
    # save_path = ConfigFileWrite(conf_data=conf, conf_type='hocon', save_file=save_file).write_conf()
    # save_path = ConfigFileWrite(conf_data=conf, conf_type='properties', save_file=save_file).write_conf()

