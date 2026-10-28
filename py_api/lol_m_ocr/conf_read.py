# -*- coding:UTF-8 -*-

"""
 @ProjectName  : config_read_write
 @FileName     : config_read_write.py
 @Description: 
 @Time         : 2021/6/8 11:44
 @Author       : Qredsun
 @Author_email : 1410672725@qq.com  
 """
import json
import os
from configparser import ConfigParser

# import toml
import yaml
from pyhocon import ConfigFactory
from pyhocon import HOCONConverter

# from logging import Logger

# logger = Logger('config_read-write').getlog()
# local_dir = os.path.dirname(os.path.abspath(__file__))

FILE_TYPE = ['toml', 'TOML', 'hocon', 'HOCON', 'json', 'JSON', 'yaml', 'YAML', 'ini', 'INI', 'properties', 'PROPERTIES']

class ConfigFileRead():
    def __init__(self, config_path, conf_type):
        self.config_path = config_path
        self.conf_type = conf_type

    def read_conf(self):
        """
        根据传入的文件类型，调用对应的方法对文件进行解析
        :return: dict config_data
        """
        if self.conf_type == 'toml' or self.conf_type == 'TOML':
            conf_data = self.read_config_toml(self.config_path)
        elif self.conf_type == 'hocon' or self.conf_type == 'HOCON':
            conf_data = self.read_config_hocon(self.config_path)
        elif self.conf_type == 'json' or self.conf_type == 'JSON':
            conf_data = self.read_config_json(self.config_path)
        elif self.conf_type == 'yaml' or self.conf_type == 'YAML':
            conf_data = self.read_config_yaml(self.config_path)
        elif self.conf_type == 'ini' or self.conf_type == 'INI':
            conf_data = self.read_config_ini(self.config_path)
        elif self.conf_type == 'properties' or self.conf_type == 'PROPERTIES':
            conf_data = self.read_config_properties(self.config_path)
        else:
            logger.error('读取文件类型不支持。支持的文件类型{}'.format(self.conf_type))
            return False

        return conf_data

    @staticmethod
    def read_config_yaml(config_path):
        """
        读取配置文件
        :param str config_path: 配置文件路径
        :return: dict config_data
        """
        # config_data = OrderedDict(dict())
        config_data = {}
        if not config_path or not os.path.isfile(config_path):
            logger.error("配置文件 {} 不存在".format(config_path))
            return False

        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = f.read()
                if float(yaml.__version__) <= 5.1:
                    config_data = yaml.load(config)
                else:
                    config_data = yaml.load(config, Loader=yaml.FullLoader)
        except Exception as e:
            logger.error("配置文件无法正常解析: {}".format(str(e)))
            return False
        return config_data

    @staticmethod
    def read_config_ini(config_path):
        """
        读取配置文件
        :param str config_path: 配置文件路径
        :return: dict config_data
        """
        # config_data = OrderedDict(dict())
        config_data = {}
        if not config_path or not os.path.isfile(config_path):
            logger.error("配置文件 {} 不存在".format(config_path))
            return False

        try:
            config = ConfigParser()
            config.read(config_path, encoding='utf-8')
            for section in config.sections():
                # config_data[section] = OrderedDict(dict())
                config_data[section] = {}
                for key, val in config.items(section):
                    config_data[section][key] = val
        except Exception as e:
            logger.error("配置文件无法正常解析: {}".format(str(e)))
            return False
        return config_data

    @staticmethod
    def read_config_toml(config_path):
        """
        读取配置文件
        :param str config_path: 配置文件路径
        :return: dict config_data
        """
        # config_data = OrderedDict(dict())
        config_data = {}
        if not config_path or not os.path.isfile(config_path):
            logger.error("配置文件 {} 不存在".format(config_path))
            return False

        try:
            config_data = toml.load(config_path)
        except Exception as e:
            logger.error("配置文件无法正常解析: {}".format(str(e)))
            return False
        return config_data

    @staticmethod
    def read_config_hocon(config_path):
        """
        读取配置文件
        :param str config_path: 配置文件路径
        :return: dict config_data
        """
        # config_data = OrderedDict(dict())
        config_data = {}
        if not config_path or not os.path.isfile(config_path):
            logger.error("配置文件 {} 不存在".format(config_path))
            return False

        try:
            config_data = ConfigFactory.parse_file(config_path)
            config_data = json.loads(HOCONConverter.to_json(config_data))
        except Exception as e:
            logger.error("配置文件无法正常解析: {}".format(str(e)))
            return False
        return config_data

    @staticmethod
    def read_config_json(config_path):
        """
        读取配置文件
        :param str config_path: 配置文件路径
        :return: dict config_data
        """
        # config_data = OrderedDict(dict())
        config_data = {}
        if not config_path or not os.path.isfile(config_path):
            logger.error("配置文件 {} 不存在".format(config_path))
            return False

        try:
            with open(config_path) as fp:
                config_data = json.load(fp)
        except Exception as e:
            logger.error("配置文件无法正常解析: {}".format(str(e)))
            return False
        return config_data

    @staticmethod
    def read_config_properties(config_path):
        """
        读取配置文件
        :param str config_path: 配置文件路径
        :return: dict config_data
        """
        # config_data = OrderedDict(dict())
        config_data = {}
        def __getDict(strName, dictName, value):
            if (strName.find('.') > 0):
                # key如果有层级，分层处理
                k = strName.split('.')[0]
                dictName.setdefault(k, {})
                return __getDict(strName[len(k) + 1:], dictName[k], value)
            else:
                dictName[strName] = value
                return dictName

        if not config_path or not os.path.isfile(config_path):
            logger.error("配置文件 {} 不存在".format(config_path))
            return False

        try:
            with open(config_path, 'r', encoding='utf-8') as pro_file:
                for line in pro_file.readlines():
                    # 逐行解析
                    line = line.strip().replace('\n', '')
                    if line.find("#") != -1:
                        # 截取行尾的注释
                        line = line[0:line.find('#')]
                    if line.find('=') > 0:
                        # 根据 = 将key 和value 分割
                        strs = line.split('=')
                        strs[1] = line[len(strs[0]) + 1:]
                        __getDict(strs[0].strip(), config_data, strs[1].strip())
        except Exception as e:
            logger.error("配置文件无法正常解析: {}".format(str(e)))
            return False
        return config_data

if __name__ == '__main__':

    save_ini = r'D:\work\bussiness\dd.ini'
    save_file = r'D:\work\dd.yaml'

    # ConfigFileRead.read_config_yaml(save_file)
    conf = ConfigFileRead.read_config_ini(save_ini)
    # ConfigFileRead.read_config_json()

    # conf = ConfigFileRead.read_config_hocon(save_file)
    # conf = ConfigFileRead.read_config_toml(monitor_log_config)
    # conf = ConfigFileRead.read_config_properties(monitor_log_config)
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
