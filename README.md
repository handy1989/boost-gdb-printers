# README
脚本从以下地址下载  
http://sourceforge.net/projects/boost-gdb-printers/  
修改文件为  
v1_52/lib/unordered.py  
diff如下  

    62c62
    <         allocators = self.value['table_']['allocators_'].type.fields()
    ---
    >         allocators = table.type['allocators_']
    65,66c65,66
    <         self.node_type = self.value['table_']['allocators_'].type.template_argument(1).template_argument(0)
    <         bucket_type = self.value['table_']['allocators_'].type.template_argument(0).template_argument(0).strip_typedefs()
    ---
    >         self.node_type = allocators.type.template_argument(1).template_argument(0)
    >         bucket_type = allocators.type.template_argument(0).template_argument(0).strip_typedefs()
